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


data1 = {'a': 4, 'b': 5}
data2 = {'b': 6, 'c': 7}
chain = ChainMap(data1, data2)
chain.parents['e'] = 8
print(chain)
