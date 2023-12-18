from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import requests
import sys
import io
import re
# from selenium import webdriver

# opts = webdriver.FirefoxOptions()
# opts.headless = True
# driver = webdriver.Firefox(options=opts)
base_url = 'http://housing-ru.task-sss.krasilnikov.spb.ru/74ca370079f9b8a16f111e4f943bfe24'
session = requests.Session()
# хидера гет запроса нужны нам для обхода cloudflare
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}


# возвращает объект BeautifulSoup по ссылке
def get_page(url):
    # checking for status code
    rq = session.get(url, headers=headers, timeout=10)
    if rq.status_code == 200:
        # parse the page
        return BeautifulSoup(rq.text, 'html.parser')
    else:
        # terminate if failed to get the page
        print(f'Failed to get {base_url} with status code {rq.status_code}')
        sys.exit(1)


# возвращает список ссылок в объекте BeautifulSoup
def find_hrefs(content):
    # get all hrefs to other locations
    __hrefs = list()
    print('Searching for hrefs...')
    for a in content.find_all('a', href=True):
        __hrefs.append(a['href'])
    return __hrefs


page_root = get_page(base_url)
base_hrefs = find_hrefs(page_root)
hrefs = base_hrefs


# check for already visited pages
visited = []
def exhaust_hrefs(base_url_str, hrefs_list):
    for __href in hrefs_list:
        if __href in visited:
            continue
        visited.append(__href)
        t = find_hrefs(get_page(urljoin(base_url, __href)))
        for h in t:
            if h not in hrefs_list:
                hrefs_list.append(h)
    return hrefs_list


# no recursion here, just a loop with fixed depth
# не очень элегантно, и не оптимально по времени выполнения
for i in range(10):
    hrefs = exhaust_hrefs(base_url, hrefs)

print(f'Found {len(hrefs)} links')

# join with base url
hrefs = [urljoin(base_url, href) for href in hrefs]


# parse simple html table
def find_simple_table(__url):
    return get_page(__url).find('table').find('table')


mandatory = pd.DataFrame()
for url in hrefs:
    simple_table = find_simple_table(url)
    if simple_table is not None:
        print(f"Found table in ...{url[len(url) - 5::]}")
        # join dataframes
        mandatory = pd.concat([mandatory, pd.read_html(io.StringIO(simple_table.prettify()))[0]])
    else:
        print(f"No table in ...{url[len(url) - 5::]}!")


def find_hidden_table_url(__url, pattern_keyword):
    csv_regex = r"\/" + pattern_keyword + r"\/[a-z-A-Z0-9]+\?[a-zA-Z]+=[0-9]+"
    pattern = re.compile(csv_regex, re.IGNORECASE | re.DOTALL | re.MULTILINE)
    content = get_page(__url).find_all('script')[1].text
    return re.findall(pattern, content)[0]


csv_urls = list()
text_urls = list()
for url in hrefs:
    hidden_table_url = find_hidden_table_url(url, 'csv')
    non_mandatory_table_url = find_hidden_table_url(url, 'text')
    if hidden_table_url is not None:
        print(f"Found csv url: {hidden_table_url}")
        csv_urls.append(urljoin(url, hidden_table_url))
    if non_mandatory_table_url is not None:
        print(f"Found text url: {non_mandatory_table_url}")
        text_urls.append(urljoin(url, non_mandatory_table_url))

for csv_url in csv_urls:
    csv_raw = get_page(csv_url)
    # remove all exclamations
    csv = str(csv_raw.text).replace('!', '')
    df = pd.read_csv(io.StringIO(csv))
    # concat with mandatory
    mandatory = pd.concat([mandatory, df])


def add_linebreak_after_n_words(input_string, n):
    words = input_string.split(', ')
    new_string = ''

    for i, word in enumerate(words):
        if i > 0 and i % n == 0:
            new_string = new_string.rstrip(', ')  # Remove the comma before line break
            new_string += '\n'
        new_string += word + ', '

    return new_string.rstrip(', ')  # Remove trailing comma


non_mandatory = pd.DataFrame()

for text_url in text_urls:
    text_raw = get_page(text_url)
    # remove all non-white words
    # no very elegant =)
    white_list = ["Id", "Utilities", "LotConfig", "LandSlope", "FR2", "CulDSac", "FR3", "AllPub", "Inside", "Gtl",
                  "Mod", "Sev", "Corner", "NaN"]
    text = ' '.join([word for word in str(text_raw.text).split() if word.isdigit() or word in white_list])
    # add comma after all words
    text = text.replace(' ', ', ')
    text = add_linebreak_after_n_words(text, 4)
    df = pd.read_csv(io.StringIO(text))
    # concat with non_mandatory
    non_mandatory = pd.concat([non_mandatory, df])

data = pd.concat([mandatory, non_mandatory])
print(data)