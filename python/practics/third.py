# -- task 3 --
"""
You are provided with a dict dishes, containing info about people and their dishes. Each key represents some dish,
and the value is a list of tuples of type (Name: str, Proportion: float). For example, (Alexa, 1) means that Alexa
ordered 1 portion of the dish, and (George, 1/2) means that George ordered half of a portion of the dish.

Also, you have a dict bill, where the info about total price of the dish is stored.
You have to return a dict payments containing participants names as keys and the amount they owe as values.
For each dish you should split its price from the bill proportionally to the number of portions they've eaten.
For example, if the cost of chicken is 1'000 rubles, and Marc consumed 2 portions, while Alexa and George each
consumed 1 portion, Marc will owe 500 rubles, Alexa - 250 rubles, and George - 250 rubles. ((((bill is for total count, not for single pt))))

Round the split amount to two decimal places.
TEST CASE:
INPUT:
dishes = {
    'chicken': [('Alexa', 1), ('George', 1), ('Marc', 2)],
    'chips': [('Alexa', 1), ('George', 1/2), ('Marc', 1/2)],
    'ice cream': [('Alexa', 1)],
    'tea': [('Alexa', 1), ('George', 1), ('Marc', 1)]
}
bill = {
    'chicken': 1000,
    'chips': 500,
    'ice cream': 200,
    'tea': 300
}

EXPECTED:
payments = {
    'Alexa': 800.0,
    'George': 475.0,
    'Marc': 725.0
}
"""

dishes = {
    'chicken': [('Alexa', 1), ('George', 1), ('Marc', 2)],
    'chips': [('Alexa', 1), ('George', 1/2), ('Marc', 1/2)],
    'ice cream': [('Alexa', 1)],
    'tea': [('Alexa', 1), ('George', 1), ('Marc', 1)]
}
bill = {
    'chicken': 1000,
    'chips': 500,
    'ice cream': 200,
    'tea': 300
}

payments = dict()
for key, value in dishes.items():
    total_count = float(sum(portion for name, portion in value))
    for name, portion in value:
        if payments.get(name) is None:
            payments[name] = float(portion / total_count * bill[key])
        else:
            payments[name] += float(portion / total_count * bill[key])
payments = {key: round(value, 2) for key, value in payments.items()}
# print(payments)