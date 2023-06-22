# # # # def is_palindrome(word):
# # # #     word = word.lower()
# # # #     return word == word[::-1]
# # # #
# # # #
# # # # def foo(a, b='world'):
# # # #     print(a)
# # # #     print(b)
# # # #
# # # #
# # # # def bar(a, b=None):
# # # #     if b is None:
# # # #         b = []
# # # #     b.append(a)
# # # #     print(b)
# # # #
# # # #
# # # # def baz(*args):
# # # #     print(args)
# # # #
# # # #
# # # # def func(**kwargs):
# # # #     print(kwargs)
# # # #
# # # #
# # # # def func2(a, b=2, *args, c=None, **kwargs):
# # # #     print(a)
# # # #     print(b)
# # # #     print(args)
# # # #     print(c)
# # # #     print(kwargs)
# # # #
# # # #
# # # # # func2(1, 2, 3, 4, 5, 6, 7, 8, c=9, e=0)
# # #
# # #
# # # def foo():
# # #     def bar():
# # #         print('bar')
# # #
# # #     bar()
# # #
# # #
# # # # LEGB
# # # a = 5
# # #
# # #
# # # def baz():
# # #     a = 4
# # #
# # #     def bar():
# # #         print(a)
# # #         print(locals())
# # #
# # #         def bam():
# # #             nonlocal a
# # #             # pass
# # #             print(a)
# # #
# # #         bam()
# # #
# # #     bar()
# # #
# # #
# # # def func():
# # #     c = 4
# # #     print(locals())
# # #
# # #
# # # b = globals().get('func')
# # #
# # # # multiply = lambda x, y: x * y
# # # # res = multiply(2, 4)
# # #
# # # # TODO Вводятся числа с клавиатуры (input) через пробел
# # # #  необходимо привести к списку чисел
# # #
# # # # numbers = input().split()
# # # # result = map(lambda x: int(x) * 2, numbers)
# # # # result2 = (int(i) * 2 for i in numbers)
# # # # print(result2)
# # # # result = []
# # # # for number in numbers:
# # # #     result.append(int(number) * 2)
# # #
# # #
# # objs = [2, 3, 4, 'hello', 'world', True, None, 'python']
# # # result = map(lambda x: x.upper(), filter(lambda x: isinstance(x, str), objs))
# # result2 = (i.upper() for i in objs if isinstance(i, str))
# # #
# #
# # text = 'hello world'
# # t = (2, 3, 4, 5, 6)
# # from itertools import zip_longest
# # z = zip_longest(result2, t, text, fillvalue='элемента не хватило')
# # print(list(z))
#
#
# # from functools import reduce
# #
# #
# # numbers = [2, '3', 4, '5', '6', 7, 8, 9]
# #
# # res = reduce(lambda x, y: int(x) + int(y), numbers)
# # print(res)
#
#
# # numbers = ['Hello', 'world', 'apple', 'Pycharm']
# # numbers.sort(key=lambda x: x.lower())
# # # ['hello', 'world', 'apple', 'pycharm']
# # print(numbers)
#
#
# # numbers = [1, 2, '3', '56', -2324, '456']
# # numbers.sort(key=lambda x: int(x))
# # print(numbers)
# # print(max(numbers, key=lambda x: int(x)))
#
#
# # users = [
# #     {'name': 'Alex', 'age': 34},
# #     {'name': 'Max', 'age': 4},
# #     {'name': 'Alena', 'age': 18},
# #     {'name': 'Pavel', 'age': 54},
# # ]
# # print([*(user for user in users if user.get('name').lower()[0] == 'a')])
# # print(*filter(lambda user: user.get('name').lower()[0] == 'a', users))
# # print(*(user for user in users if user.get('name').lower()[0] == 'a'))
# # old_user = max(filter(lambda user: user.get('name').lower()[0] == 'a', users), key=lambda x: x.get('age'))
# # print(old_user)
#
#
# # def foo(a, b, c):
# #     print(a * b * c)
#
#
# # args = [3, 7, 5]
# # foo(args[0], args[1], args[2])
# kwargs = {
#     'a': 5,
#     'b': 2,
#     'c': 8
# }
# # res = [*kwargs.items()]
# # print(res)
# # foo(a=kwargs['a'], b=kwargs['b'], c=kwargs['c'])
# # foo(**kwargs)
#
# text = 'hello world'
# # symbols = list(text)
# # symbols = [*text]
# symbols = [i for i in text]
# print(symbols)


def foo():
    a = 4

# FIFO
# LIFO
