# -- task 6 --
"""
Final mark formula:
FinalMark = 0.4 * O1 + 0.6 * O2
    where O1 is an average grade for all Seminar tasks
      and O2 is an average grade for all Test tasks
FinalMark is rounded to integer with mathematical rules, e.g. 6.5 = 7, 6.49 = 6
Seminar tasks cannot be retaken regardless of the reason of absence (if student missed the seminar task,
he obtains zero for that task).
However, if student misses the Test task FOR VALID REASON (and does not receive a grade for that Test activity) -
the O2 grade is recalculated without that particular Test task.
Calculate final mark for each student (the output variable should be pandas.Series of integers with indexes containing
student names sorted alphabetically) and put the output in the variable `result`.

Hints:
    - you are given with 3 pandas.DataFrame
    - the course structure and schedule are placed in `plan` variable (at least one Seminar and one Test task is guaranteed)
    - student grades are stored in `grades` variable (missed classes are represented with NaN). Student names are unique.
      All dates stored in string format.
    - the table of excuses and their status stored in `excuses` variable

TEST CASE:
INPUT:
grades = pd.DataFrame({
    '2017-02-05': {'Hermione': 5, 'Ron': 2},
    '2017-02-12': {'Hermione': float('nan'), 'Ron': float('nan')},
    '2017-02-19': {'Hermione': 7.0, 'Ron': float('nan')},
    '2017-02-26': {'Hermione': float('nan'), 'Ron': 4.0},
})

plan = pd.DataFrame({
    'activity': {0: 'Test', 1: 'Test', 2: 'Seminar', 3: 'Seminar'},
    'date': {0: '2017-02-05', 1: '2017-02-12', 2: '2017-02-19', 3: '2017-02-26'},
})

excuses = pd.DataFrame({
    'name': {0: 'Hermione', 1: 'Hermione', 2: 'Ron', 3: 'Harry'},
    'date': {0: '2017-02-05', 1: '2017-02-12', 2: '2017-02-19', 3: '2017-02-19'},
    'reason': {0: 'valid', 1: 'valid', 2: 'invalid', 3: 'invalid'},
})

OUTPUT:
result = pd.Series({
    'Hermione': 4,
    'Ron': 1,
})
"""

import pandas as pd

grades = pd.DataFrame({
    '2017-02-05': {'Hermione': 5, 'Ron': 2},
    '2017-02-12': {'Hermione': float('nan'), 'Ron': float('nan')},
    '2017-02-19': {'Hermione': 7.0, 'Ron': float('nan')},
    '2017-02-26': {'Hermione': float('nan'), 'Ron': 4.0},
})

plan = pd.DataFrame({
    'activity': {0: 'Test', 1: 'Test', 2: 'Seminar', 3: 'Seminar'},
    'date': {0: '2017-02-05', 1: '2017-02-12', 2: '2017-02-19', 3: '2017-02-26'},
})

excuses = pd.DataFrame({
    'name': {0: 'Hermione', 1: 'Hermione', 2: 'Ron', 3: 'Harry'},
    'date': {0: '2017-02-05', 1: '2017-02-12', 2: '2017-02-19', 3: '2017-02-19'},
    'reason': {0: 'valid', 1: 'valid', 2: 'invalid', 3: 'invalid'},
})


class Mark:
    def __init__(self, activity, value):
        self.activity = activity
        self.mark = value

    mark = 0
    activity = ''


def append_mark(__marks, __name, __mark):
    if __name in __marks.keys():
        __marks[__name].append(__mark)
    else:
        __marks[__name] = [__mark]


marks = dict()
for date in grades.to_dict().keys():
    for name, mark in grades[date].items():
        # get activity type and weight
        __activity = plan[plan['date'] == date]['activity'].values[0]
        if pd.isna(mark):
            # check for valid excuse for name, date
            reason = excuses[(excuses['name'] == name) & (excuses['date'] == date)]['reason']
            if len(reason) == 0:
                reason = 'invalid'
            else:
                reason = reason.values[0]
            if reason == 'valid':
                if __activity == 'Seminar':
                    append_mark(marks, name, Mark(__activity, 0))
                else:
                    pass
            else:
                append_mark(marks, name, Mark(__activity, 0))
        else:
            append_mark(marks, name, Mark(__activity, mark))

seminars = dict()
tests = dict()
for name, mark in marks.items():
    for m in mark:
        if m.activity == 'Seminar':
            if name in seminars.keys():
                seminars[name].append(m.mark)
            else:
                seminars[name] = [m.mark]
        else:
            if name in tests.keys():
                tests[name].append(m.mark)
            else:
                tests[name] = [m.mark]

for name in seminars.keys():
    seminars[name] = sum(seminars[name]) / len(seminars[name]) * 0.4
for name in tests.keys():
    tests[name] = sum(tests[name]) / len(tests[name]) * 0.6

final_marks = dict()
for name in seminars.keys():
    if name in final_marks.keys():
        final_marks[name] += seminars[name]
    else:
        final_marks[name] = seminars[name]
for name in tests.keys():
    if name in final_marks.keys():
        final_marks[name] += tests[name]
    else:
        final_marks[name] = tests[name]
for name in final_marks.keys():
    final_marks[name] = int(round(final_marks[name], 0))

result = pd.Series(final_marks)