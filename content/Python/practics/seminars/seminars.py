# drink = input()
# if drink == 'tea':
#     result = '100 rub'
# elif drink == 'coffee':
#     result = '150 rub'
# else:
#     result = 'no drink'
# print(result)

# x = int(input())
# y = int(input())
# quadrant = 0
# if x > 0 and y > 0:
#     quadrant = 1
# elif x < 0 and y > 0:
#     quadrant = 2
# elif x < 0 and y < 0:
#     quadrant = 3
# else:
#     quadrant = 4
# print(quadrant)

# x = int(input())
# y = int(input())
# r = int(input())
# if x ** 2 + y ** 2 <= r ** 2:
#     in_circle = True
# else:
#     in_circle = False
# print(in_circle)

# a = float(input())
# b = float(input())
# c = float(input())
#
# if int(a) == 0:
#     x0, y0 = False, False
# else:
#     x0 = -b / 2 * a
#     y0 = c - b * b / 4 * a
# print(f'{x0} {y0}')

# a = float(input())
# b = float(input())
# c = float(input())
#
# # D = b*b - 4ac
# # x = -b +- sqrt(D) / 2a
#
# disc = b ** 2 - 4 * a * c
# if disc < 0:
#     x1, x2 = False, False
# elif disc == 0:
#     x1 = (-b + pow(disc, 0.5)) / (2 * a)
#     x2 = False
# else:
#     x1 = (-b + pow(disc, 0.5)) / (2 * a)
#     x2 = (-b - pow(disc, 0.5)) / (2 * a)
# print(f'{x1} {x2}')