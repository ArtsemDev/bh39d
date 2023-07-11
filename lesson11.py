# # def decorator(*decorator_args):
# #
# #     def wrapper(func):
# #
# #         def wrapped(*args):
# #             print('pre process')
# #             res = func(*args)
# #             print('post process')
# #             return res
# #
# #         return wrapped
# #
# #     return wrapper
# #
# #
# # @decorator()
# # def foo():
# #     print(2 + 2)
# #
# #     # @decorator()
# #     def bar():
# #         pass
# #
# #     bar()
# #
# #
# # @decorator()
# # def baz():
# #     pass
# #
# #
# # # text = 'Hello World'
# # # text = text.lower()
# #
# # # data = {i: text.lower().count(i) for i in text.lower() if i.isalpha()}
# # # numbers = [i ** 2 for i in range(1, 100)]
# # # data = {}
# # # for i in text:
# # #     if i.isalpha():
# # #         data[i] = text.count(i)
# #
# #
# # # from itertools import count, repeat
# # #
# # #
# # # count()
# # # repeat()
# #
# #
# # from utils import *
# # #
# # #
# # # main_func1()
# # # my_range()
# #
# #
# # # if __name__ == '__main__':
# # #     print(__name__)
# # # from copy import deepcopy, copy
# # #
# # # c = [1, 2, 3]
# # # d = [4, 5, 6]
# # #
# # # a = [c, d]
# # # b = deepcopy(a)
# #
# # from itertools import *
# #
# #
# # # for i in count(5, -3):
# # #     print(i)
# #
# #
# # # for i in cycle('hello'):
# # #     print(i)
# #
# #
# # # for i in repeat('hello', 5):  # ('hello', 'hello', 'hello', 'hello', 'hello')
# # #     print(i)
# #
# #
# # # print(list(repeat('hello', 5)))
# #
# # # print(list(combinations([1, 2, 3, 4], 3)))
# # # print(list(combinations_with_replacement([1, 2, 3, 4], 2)))
# # # print(list(permutations([1, 2, 3, 4], 2)))
# # # print(list(product((1, 2, 3), (4, 5, 6), (7, 8, 9))))
# #
# # # print(list(filterfalse(lambda x: x % 2, [1, 2, 3, 4, 5])))
# # # print(list(dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5])))
# # # print(list(takewhile(lambda x: x < 3, [1, 2, 3, 4, 5])))
# #
# #
# # # print(list(compress([1, 2, 3, 4], ('', 56, 'qwert', False))))
# #
# #
# # # names = ('Vasya', 'Petya', 'Masha')
# # # emails = ('vasya@gmail.com', None, 'masha@yandex.ru')
# # #
# # # print(list(compress(names, emails)))
# #
# #
# # # for i in chain('hello', (1, 2, 3, 4), ['hello', 'world']):
# # #     print(i)
# #
# #
# # # for i in islice('hello', 0, len('hello'), 1):
# # # # for i in 'hello'[:3]:
# # #     print(i)
# #
# # #
# # # for i in tee([1, 2, 3, 4], 5):
# # #     for j in i:
# # #         print(j)
# # #
# #
# #
# # # data = [
# # #     ({'name': 'Vasya1', 'role_id': 5}),
# # #     ({'name': 'Vasya2', 'role_id': 3}),
# # #     ({'name': 'Vasya3', 'role_id': 4}),
# # #     ({'name': 'Vasya4', 'role_id': 4}),
# # #     ({'name': 'Vasya5', 'role_id': 3}),
# # #     ({'name': 'Vasya6', 'role_id': 5}),
# # # ]
# # #
# # # for i, j in list(groupby(data, key=lambda x: x.get('role_id'))):
# # #     print(list(j))
# #
# #
# # # print(list(accumulate([1, 2, 3, 4, 5], lambda x, y: x * y)))
# #
# #
# # # from math import *
# # # from random import *
# # #
# # #
# # # from os import name, system
# # #
# # #
# # # system('ls -a')
# # # from os.path import join
# #
# #
# # # from sys import *
# #
# # from pathlib import Path
# #
# #
# # BASE_DIR = Path(__file__).resolve().parent
# # file_path = BASE_DIR / 'inputeeeee.txt'
# # # file_path.touch()
# # # with file_path.open('r', encoding='utf-8') as file:
# # #     print(file.read())
#
#
# # from datetime import datetime, date, time, timedelta
# #
# #
# # d = datetime.utcnow()
# # print(timedelta(days=5).total_seconds())
#
# # print(d - d)
# # print(d.timestamp())
# # print(d.isoformat())
# # print(d.strftime('%B --- %w %Y %H,%M,%S'))
# # print(datetime.strptime('July --- 2 2023 09,44,38', '%B --- %w %Y %H,%M,%S'))
#
# # d = '04.05.2020 14:56:58'
# # d = datetime.strptime(d, '%d.%m.%Y %H:%M:%S')
# # print(d)
#
# from dataclasses import dataclass
# from enum import Enum
#
# status = 201
#
# # if status == HTTPStatus.CREATED:
# #     print('create')
#
#
# class Role(int, Enum):
#     ADMIN = 0
#     MANAGER = 1
#     USER = 2
#
#
# @dataclass(frozen=True)
# class User:
#     name: str
#     role_id: int
#
#
# vasya = User(name='vasya', role_id=1)
#
# if vasya.role_id == Role.MANAGER:
#     pass


# from argparse import ArgumentParser
#
#
# parser = ArgumentParser()
# parser.add_argument('--host', default='127.0.0.1', help='Project host')
# parser.add_argument('-d', '--debug', action='store_true', help='Debug Mode')
# parser.add_argument('-f', '--foo', action='store_true', help='Foo Mode')
# parser.add_argument('-p', '--port', default=8000)
# args = parser.parse_args()
# print(args)


# import logging
#
# logging.basicConfig(
#     filename='log.log',
#     filemode='a',
#     format='%(asctime)s - [%(levelname)s] - %(filename)s - %(lineno)s - %(funcName)s | %(message)s',
#     level='INFO'
# )
#
# logging.info('Hello')

