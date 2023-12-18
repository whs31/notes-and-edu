# -- 4 --
"""
Given var `intros` (T: str) where students introduce themselves.
Task: create dict `info` with following keys:
    - "name" = list with students names (T: list<str>)
    - "surname" = list with students surnames (T: list<str>)
    - "age" = list with students ages (T: list<int>)
    - "major" = list with students majors (T: list<tuple<str, int>>)
SORT BY SURNAMES

TEST CASE:
INPUT:
intros = "Hi! Nice to meet you! My name is Maxim Petrov. I'm 20 years old. I am a 3rd-year Economics student.
          Hi! Nice to meet you! My name is Maria Ivanova. I'm 19 years old. I am a 2nd-year Arts and Design student."

EXPECTED:
info = {
    "name": ["Maria", "Maxim"],
    "surname": ["Ivanova", "Petrov"],
    "age": [19, 20],
    "major": [("Arts and Design", 2), ("Economics", 3)]
}
"""

intros = """
            Hi! Nice to meet you! My name is Maxim Petrov. I'm 20 years old. I am a 3rd-year Economics student.
            Hi! Nice to meet you! My name is Maria Ivanova. I'm 19 years old. I am a 2nd-year Arts and Design student.
         """

info = dict()
info['name'] = []
info['surname'] = []
info['age'] = []
info['major'] = []
split = intros.replace('\n', ' ').split('student.')
split = [student.strip() for student in split if student]
if split[-1] == '':
    del split[-1]
for raw in split:
    i = raw.find("My name is") + len("My name is")
    full_name = raw[i:raw.find(".", i)].strip()
    surname = full_name.split()[-1]
    name = ' '.join(full_name.split()[:-1])

    j = raw.find("I'm") + len("I'm")
    age = int(raw[j:raw.find("years old", j)].strip())

    k = raw.find("I am a") + len("I am a")
    major_str = raw[k:].strip()
    parts = major_str.split()
    year_str = parts[0]
    year = int(year_str[:1])
    major_name = ' '.join(parts[1:])
    major = tuple((major_name, year))

    info['name'].append(name)
    info['surname'].append(surname)
    info['age'].append(age)
    info['major'].append(major)

sorted_data = sorted(zip(info["surname"], zip(info["name"], info["age"], info["major"])))
sorted_info = {
    "name": [name for surname, (name, _, _) in sorted_data],
    "surname": [surname for surname, _ in sorted_data],
    "age": [age for _, (_, age, _) in sorted_data],
    "major": [(major, year) for _, (_, _, (major, year)) in sorted_data]
}
info = sorted_info
# print(info)