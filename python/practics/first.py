# -- task 1 --
"""
You are given a list actors_and_oscars. The list consists of strings containing the names of the actors,
the titles of the films for which the Oscars were awarded, the films release years and the countries
of the production. These elements in each string are separated in three ways: with a semicolon, slash or a point.
The structure of actors_and_oscars list:
[
    'actor_name; film_title; release_year; country',
    'actor_name/ film_title/ release_year/ country',
    'actor_name. film_title. release_year. country',
    # ...
]
Actors and titles can be any Unicode (except control characters, described above).
You have to create a dict correct_oscars with corrected information and this structure:
{
    "actor_name": [
        "film_title_1",
        "release_year_1",
        "country_1",
    ],
    # ...
}
The title in correct oscars cannot contain:
    - any digits
    - sequences of capital letters
    - extra spaces
Type of release year must be casted to int
Strings with actor and country names must be trimmed (no extra spaces)

TEST CASE:
INPUT:
actors_and_oscars = [
    'Katharine Hepburn   ;      OOOOOn Go78833lden Pond     ; 1981; USA',
    'Julianne Moore; Sti2ll AAAAli23ce; 2014; France',
    ' Ingrid Bergman / Mur35der on the Orie89nt EExpress/ 1974/ UK ',
    'Phillip Seymour Hoffman; Cap0ote;2005 ; Canada       ',
    ' Olivia Colman    .The Favourite.    2018 . Ireland',
    'Scarlett Ingrid Johansson. Marriage Story. 2019.      UK'
]

EXPECTED:
correct_oscars = {
    'Katharine Hepburn': ['On Golden Pond', 1981, 'USA'],
    'Julianne Moore': ['Still Alice', 2014, 'France'],
    'Ingrid Bergman': ['Murder on the Orient Express', 1974, 'UK'],
    'Phillip Seymour Hoffman': ['Capote', 2005, 'Canada'],
    'Olivia Colman': ['The Favourite', 2018, 'Ireland'],
    'Scarlett Ingrid Johansson': ['Marriage Story', 2019, 'UK']
}
"""

actors_and_oscars = [
    'Katharine Hepburn   ;      OOOOOn Go78833lden Pond     ; 1981; USA',
    'Julianne Moore; Sti2ll AAAAli23ce; 2014; France',
    ' Ingrid Bergman / Mur35der on the Orie89nt EExpress/ 1974/ UK ',
    'Phillip Seymour Hoffman; Cap0ote;2005 ; Canada       ',
    ' Olivia Colman    .The Favourite.    2018 . Ireland',
    'Scarlett Ingrid Johansson. Marriage Story. 2019.      UK'
]


correct_oscars = dict()
for nt_str in actors_and_oscars:
    char_mapping = {';': ';', '/': '/', '.': ''}
    control_char = next((char for char, mapping_char in char_mapping.items() if nt_str.count(mapping_char) > 0), '')

    split = nt_str.split(control_char)
    name = split[0].strip()
    title = split[1].strip()
    year = int(split[2].strip())
    country = split[3].strip()

    # remove digits from title
    title = ''.join([char for char in title if not char.isdigit()])
    rm_unnecessary_caps = lambda s: ''.join(char if not (char.isupper() and (i > 0 and char == s[i - 1]))
                                            else '' for i, char in enumerate(s))
    title = rm_unnecessary_caps(title)
    correct_oscars[name] = [title, year, country]
