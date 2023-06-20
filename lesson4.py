# objs = [2, 4, 2, 'Hello', 'World', True, None]
# # print(len(objs))
# # print(objs[3:6])
# objs[3] = 'Python'
# print(objs)

# text = 'hello world'
# symbols = list(text)
# print(symbols)

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = a + b
# print(c * 2)

# a = ['sss', 's', 'sssss', 'sss']
# a.sort(key=len, reverse=True)
# b = a
# a.append([1, 2, 3])
# print(a)
# a.remove('hello')
# print(a)
# b = a.pop(2)
# print(a)
# print(b)
# del a[2:]
# print(a)


# a = [1, 2, 3]
# b = [a]
# b[0].append(4)
# print(a)
# c = b.copy()
# a.append(4)
# c.append(5)
# print(b)
# print(c)


# numbers = [i / 2 for i in range(1, 101)]
# print(numbers)


# a = 1, 2, 3, 4
# print(a)
# b = ([1, 2, 3, 4], )


# a = set('hello')
# print(a)


# a = {4, 5, 6, 21, 44, 35, 8, 7, 9}
# print(a.isdisjoint([2, 3]))

# a = {1, 2, 3, 5}
# b = {3, 2, 4, 1}
# print(a.issubset(b))
# print(a <= b)
# c = a.union([5, 6, 7, 8], b)
# c = a | b
# print(c)

# print(b.difference(a))
# print(a.intersection(b, [4]))
# print(a & b)
# print(a.symmetric_difference(b))
# print(a ^ b)
# a &= b & {3, 4}
# print(a)


# c = frozenset('hello')
# c = set(c)
# c.add(5)
# c = frozenset(c)
#
# print(c)


# data = {'name': 'Alex', 'phone': 1234567890}
# data['name'] = 'Pavel'
# data['city'] = 'Minsk'
# print('city' in data)

# data = dict([('name', 'Alex'), ('city', 'Minsk'), ('languages', ['ru', 'en'])])
# print(data)
# print(dict(['ab', 'cd']))

# data = dict.fromkeys(['name', 'phone', 'city'])
# print(data)


# data = {'name': 'Alex', 'phone': 1234567890}
# print(data.get('city', 'Н/У'))
# print(data.setdefault('city', 'Н/У'))
# print(data)
# value = data.pop('city', 'Н/У')
# print(value)
# print(data)

# print(data.popitem())
# print(data)
# print(list(data.keys()))
# print(list(data.values()))
# print(list(data.items()))

# print(list(data))
# data = {'name': 'Alex', 'phone': 1234567890}
# data2 = {'city': 'Minsk', 'name': 'Max'}
# data.update(data2)
# print(data)
# result = {**data, **data2}
# result = data | data2
# print(result)

# data |= data2 | {'last_name': 'petrov'}
# print(data)
# max()

# text = 'Привет мир'
# data = {
#     'П': 'p',
#     'р': 'r',
#     'и': 'i',
#     'в': 'v',
#     'е': 'e',
#     'т': 't'
# }
# res = str.maketrans(data)
# text = text.translate(res)
# print(text)
# data = {'name': 'Alex', 'age': 45}
# text = 'Hello {name} your age {age}'.format_map(data)
# print(text)
from collections import *


# text = 'Hello World'
# counter = Counter(text)
# text2 = 'Hello Python'
# counter2 = Counter(text2)
# print(counter - counter2)
# print(counter)
# print(counter2)
# counter.subtract(counter2)
# print(counter)
# print(counter.most_common(3))
# print(list(counter.elements()))

# print(deque([1, 2, 3, 4], maxlen=2))


# data = defaultdict(list)
# print(data)
# data['languages'].append('ru')
# print(data['city'])


# User = namedtuple('User', ['name', 'age', 'city'])
#
# vasya = User(name='vasya', age=34, city='Minsk')
# print(vasya.name)
# print(vasya._asdict())


# data1 = {'a': 4, 'b': 5}
# data2 = {'b': 6, 'c': 7}
# chain = ChainMap(data1, data2)
# chain.parents['e'] = 8
# print(chain)
# text = input('Enter text: ')  # Hello
# data = {text[i]: text.count(text[i]) for i in range(len(text))}  # from 0 to len(text) [0, 5) 0, 1, 2, 3, 4
# data = {i: text.count(i) for i in text}  # from 0 to len(text) [0, 5) 0, 1, 2, 3, 4
# print(data)

# a = int(input('Enter number: '))
#
# if a > 0:
#     print('a is positive')
# elif a == 0:
#     print('a is zero')
# else:
#     print('a is negative')

# users = []
#
# if not users:
#     users.append({})

# a = 213
# if a % 2:
#     pass


# a = int(input('Enter number: '))
# is_even = 'No' if a % 2 else 'Yes' if a != 0 else 'Zero'
#
# if a % 2:
#     is_even = 'No'
# elif a != 0:
#     is_even = 'Zero'
# else:
#     is_even = 'Yes'


# BAD
# if type(5) is int:
#     print('asdf')

# BEST
# a = 5
# if isinstance(a, (str, float)):  # До python3.10
# if isinstance(a, str | float):  # Начиная с python3.10
#     print('a is digit')


# a = 5
#
# if isinstance(a, str) and a.isdigit():
#     print('a digit str')

# if a > 0 or a < 0:  # 1 + 0 = 1
#     print('a is not zeros')

# if not condition1 or condition2 and condition3:
#     pass


# x = True
# y = False
# z = False
# if not x or y:  # 0 + 0 = 0
#     print(1)  #
# elif not x or not y and z:  # 0 + 1 * 0 = 0 + 0 = 0
#     print(2)  #
# elif not x or y or not y and x:  # 0 + 0 + 1 * 1 = 0 + 0 + 1 = 1
#     print(3)  # + + + + +
# else:
#     print(4)  #

# season = 1  # from 1 to 4
# seasons = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
# print(seasons.get(season, 'invalid season number'))
#
# if season == 1:
#     print('winter')
# elif season == 2:
#     print('spring')
# elif season == 3:
#     print('summer')
# elif season == 4:
#     print('autumn')
# else:
#     print('invalid season number')

# r = range(1, 10, 2)  # 1, 3, 5, 7, 9
# print(r[2: 4])
# print(5 in r)
# print(r[1])
# print(r[2:4])
# print(r == range(10))

# for i in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     i **= 2
#     print(i, end=' ')

# text = 'hello world'
# for i in text:
#     i = i.upper()
#     print(i, end='')

# text = 'hello world'
# for i in range(len(text) - 1):
#     print(text[i], text[i+1])
# for i, j in enumerate(text):
#     print(i, j)
# data = [
#     ('a1', 'b1', 'c1'),
#     ('a2', 'b2', 'c2'),
#     ('a3', 'b3', 'c3'),
#     ('a4', 'b4', 'c4'),
#     ('a5', 'b5', 'c5'),
# ]
# for i, j, k in data:
#     print(i, j, k)

# a = (1, 2, 3, 4, 5, 6, 7)
# i, j, *k = a
# print(i, j, k)


# data = {
#     'key1': 'val1',
#     'key2': 'val2',
#     'key3': 'val3',
#     'key4': 'val4',
# }
# for key, val in data.items():
#     print(key, val)


# for i in range(10):
#     if i % 2:
#         continue
#     print(i ** 2)


# for i in range(10):
#     if i == 10:
#         break
#     print(i ** 2, end=' ')
# else:
#     print('finish!')


# number = int(input('Enter number: '))
# if number < 2:
#     print(False)
# else:
#     for i in range(2, number // 2):
#         if number % i == 0:
#             print(False)
#             break
#     else:
#         print(True)


# TODO Пользователь вводит сумму (положительное число)
#  и процентную савку по вкладу (прим 10)
#  высчитать год когда депозит удвоится
#  вклад капитализации
# from math import log, ceil
# deposit = float(input('Enter deposit: '))
# percent = float(input('Enter percent (ex: 10): ')) / 100 + 1
# target = deposit * 2
# year = 0
# # year = log(2, percent)
# # print(ceil(year))
# while deposit < target:
#     year += 1
#     deposit *= percent
# print(year)
# a = input()
# while ...:
#     pass

# numbers = [1, 2, 3, 4]
# for number in numbers:
#     numbers.append(number)


# objs = [1, 2, 3, 'hello', 'world', True, None, 'python']
# for obj in objs:
#     if not isinstance(obj, str):
#         objs.remove(obj)
# print(objs)


# words = ['hello', 'world', 'python']
# for word in words:
#     for letter in word:
#         print(letter)


# numbers = [i if i % 4 else (i ** 2) for i in range(2, 100, 2) if not i % 6]
# numbers = []
# for i in range(2, 100, 2):
#     if not i % 6:
#         if i % 4:
#             numbers.append(i)
#         else:
#             numbers.append(i ** 2)
# print(numbers)

# TODO Вводятся числа с клавиатуры через пробел
#  необходимо привести данную строку к списку чисел
# numbers = '2 4 6 5 7 2'
# numbers = [2, 4, 6, 5, 7, 2]
# VAR 1
# numbers = input('Enter numbers: ').split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers)

# VAR 2
# numbers = [int(number) for number in input('Enter numbers: ').split()]
# print(numbers)


# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError:
#     print('is not number')
# except ZeroDivisionError:
#     print('на ноль делить нельзя')
# except Exception as e:
#     print(e)
#     print('все оставшиеся ошибки')
# else:
#     print('ошибок не было')
# finally:
#     print('в любом случае')

# try:
#     a = 5
# finally:
#     pass


# raise ValueError('моя ошибка')
# TASK 1
# N = 5
# M = 3
# K = 10
# result: 12 15 18 21 24


# TASK 3
# N = 44
# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34 36 38 40
# 42 44
