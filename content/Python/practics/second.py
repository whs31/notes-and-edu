# -- task 2 --
"""
You are given dict olympic_games with the following elements structure:
    - keys are strings containing information about the city where the game was held,
      abbreviation of the host country (in round brackets), and the year of the OG (T: str)
    - values are dictionaries with the following structure:
        1. element with key "expenses" contains info about expenses of the corresponding OG (T: str)
        2. element with key "revenue" contains info about revenue of the corresponding OG (T: str)
        Note that exp/rev are written in different ways. Possible formats:
        - '$5B' = 5 billion dollars
        - '$1.5B' = 1.5 billion dollars
The structure of olympic_games dict:
{
    "host_city(abbreviation_of_country) year_of_game": {
        "expenses": "expenses_of_the_og",
        "revenue": "revenue_of_the_og"
    }, ...
}
You have to create new dict fin_results with the following structure:
    - keys are the abbreviations of the countries (T: str)
    - values are dictionaries with the following elements:
        1. element with key 'info' - a list of strings representing host cities and years of the OG in
           the corresponding country. MUST BE SORTED IN ASCENDING ORDER! (T: list<str>)
        2. element with key 'profit' or 'loss' - absolute difference between revenue and expenses in
           billions dollars rounded to 1 decimal place (T: float)
The structure of the final fin_results dict:
{
    "abbreviation_of_country": {
        "info": [
            "host_city year_1",
            "host_city year_2"
        ],
        "profit": positive_profit_in_billions,
    },
    "abbreviation_of_country": {
        "info": [
            "host_city year_1",
            "host_city year_2"
        ],
        "loss": negative_profit_in_billions,
    }, ...
}

Test case:
Input:
olympic_games = {
    'Vancouver(CAN) 2010': { 'expenses': '$7B', 'revenue': '$7.5B' },
    'Sochi(RUS) 2014': { 'expenses': '$55B', 'revenue': '$10B' },
    'Moscow(RUS) 1980': { 'expenses': '$6.3B', 'revenue': '$2.8B' },
    'Sydney(AUS) 2000': { 'expenses': '$4.2B', 'revenue': '$1.3B' }
}
Expected:
fin_results = {
    'RUS': {
        'info': [ 'Moscow 1980', 'Sochi 2014' ],
        'loss': 48.5
    },
    'CAN': {
        'info': [ 'Vancouver 2010' ],
        'profit': 0.5
    },
    'AUS': {
        'info': [ 'Sydney 2000' ],
        'loss': 2.9
    }
}
"""

olympic_games = {
    'Vancouver(CAN) 2010': {'expenses': '$7B', 'revenue': '$7.5B'},
    'Sochi(RUS) 2014': {'expenses': '$55B', 'revenue': '$10B'},
    'Moscow(RUS) 1980': {'expenses': '$6.3B', 'revenue': '$2.8B'},
    'Sydney(AUS) 2000': {'expenses': '$4.2B', 'revenue': '$1.3B'}
}

fin_results = dict()
for key, value in olympic_games.items():
    country_tag = key[key.index('(') + 1:key.index(')')]
    year = key[key.index(' ') + 1:]
    city = key[:key.index('(')]
    if fin_results.get(country_tag) is None:
        fin_results[country_tag] = dict()
        fin_results[country_tag]['info'] = [f'{city} {year}']
        revenue = float(value['revenue'][1:-1])
        expenses = float(value['expenses'][1:-1])
        if revenue < expenses:
            fin_results[country_tag]['loss'] = float(round(expenses - revenue, 1))
        else:
            fin_results[country_tag]['profit'] = float(round(revenue - expenses, 1))
    else:
        fin_results[country_tag]['info'].append(f'{city} {year}')
        revenue = float(value['revenue'][1:-1])
        expenses = float(value['expenses'][1:-1])
        if revenue < expenses:
            if fin_results[country_tag].get('loss') is None:
                fin_results[country_tag]['profit'] -= float(round(expenses - revenue, 1))
                if fin_results[country_tag]['profit'] < 0:
                    fin_results[country_tag]['loss'] = fin_results[country_tag]['profit']
                    fin_results[country_tag]['profit'] = None
            fin_results[country_tag]['loss'] += float(round(expenses - revenue, 1))
        else:
            if fin_results[country_tag].get('profit') is None:
                fin_results[country_tag]['loss'] -= float(round(revenue - expenses, 1))
                if fin_results[country_tag]['loss'] < 0:
                    fin_results[country_tag]['profit'] = fin_results[country_tag]['loss']
                    fin_results[country_tag]['loss'] = None
            fin_results[country_tag]['profit'] += float(round(revenue - expenses, 1))
for value in fin_results.values():
    value['info'].sort()
# sort fin_results by country name, that's optional but in expected test case dict is sorted somehow
fin_results = dict(sorted(fin_results.items(), reverse=True))
# print(fin_results)
