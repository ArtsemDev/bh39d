# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34

# n = int(input('enter n: '))
# c = 0
# for i in range(2, n+1, 2):
#     print(i, end=' ')
#     c += 1
#     if c == 5:
#         c = 0
#         print()

# for i in range(2, n+1, 2):
#     print(i, end=' ')
#     if i % 10 == 0:
#         print()

# for i in range(2, n+1, 10):
#     for j in range(i, i+9, 2):
#         if j > n:
#             break
#         print(j, end=' ')
#     print()

# formula = input()
# print(eval(formula))


# text = 'print("hello")'
# eval(text)

# a = int(input())
# c = input()
# b = int(input())
#
# data = {
#     '+': f'{a + b = }',
#     '-': f'{a - b = }',
#     '*': f'{a * b = }',
#     '/': f'{a / b = }',
#     '//': f'{a // b = }',
#     '**': f'{a ** b = }',
#     '%': f'{a % b = }',
# }
# print(data.get(c))


# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers) // 2):
#     # c = numbers[i]
#     # numbers[i] = numbers[~i]
#     # numbers[~i] = c
#     numbers[i], numbers[~i] = numbers[~i], numbers[i]
# print(numbers)

# n = int(input())
# names = [input('name: ') for _ in range(n)]
# emails = [input('email: ') for _ in range(n)]
# data = {i: {'name': names[i], 'email': emails[i]} for i in range(n)}

# data = {i: {'name': input('name: '), 'email': input('email ')} for i in range(n)}
# print(data)

# n = int(input('count: '))
# m = int(input('divisor: '))
# k = int(input('start: '))
# while n:
#     if k % m == 0:
#         n -= 1
#         print(k)
#         k += m
#     else:
#         k += 1


def progress(start, stop, multiply):
    while start < stop:
        yield start
        start *= multiply


def infinity_range(start, step):
    while ...:
        yield start
        start += step


def foo(a):
    if a > 0:
        print(a)
        foo(a - 1)


# numbers = [2, 3, 4, 2, 5, 4, [6, 7, 5, 6, ], [8, 7, 6, 4, 7, [6, 5, 7, 4, 5, 3, [7, 6, 5, [7, 6, 3, 4, 2, [8, 7, 6, 5, 7, ], [7, 6, 8, 5, 6, 4, 6, ]]]]]]
# numbers = [1, 2, 3, [1, 2, 3, [1, 2, 3], [1, 2, 3], [1, 2, 3]]]


def recursive_multiply(numbers):
    res = 1
    for number in numbers:
        if isinstance(number, int):
            res *= number
        else:
            res *= recursive_multiply(number)
    return res


def factorial(n):
    if n > 1:
        n *= factorial(n - 1)
    return n


def bar(a):
    def baz(b):
        def foo(c):
            return a * b * c

        return foo

    return baz


def decorator(func):
    print('decorator')

    def wrapper(a, b):
        print('Pre process')
        a += 1
        b += 2
        func(a, b)
        print('Post process')

    return wrapper


# @decorator
# def multiply(a, b):
#     print(a * b)


# decorated_multiply = decorator(multiply)


func_list = []


def is_instance(*_types):
    def wrapper(func):
        func_list.append(func)

        def wrapped(*args):
            for i in range(len(_types)):
                if not isinstance(args[i], _types[i]):
                    raise TypeError

            res = func(*args)
            return f'{res=}'

        return wrapped

    return wrapper


@is_instance(int, int)
def multiply(a, b):
    return a * b


@is_instance(str, list, bool)
def func(text, numbers, flag):
    pass


filters = {}


def dispatcher(message):
    def wrapper(func):
        filters[message] = func

        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped

    return wrapper


@dispatcher('hey')
def hello():
    print('hello')


@dispatcher('bye')
def goodbye():
    print('goodbye')


def error():
    print('error')


# from datetime import datetime
#
# start = datetime.now()
# end = datetime.now()
# print(end - start)

# TODO Написать декоратор без проброса аргументов, высчитывающий время выполнения
#  обернутой функции

def timeit(func):
    from datetime import datetime

    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        end = datetime.now()
        print(f'{func.__name__} {(end - start).seconds}s')
        return res

    return wrapper


@timeit
def foo():
    from time import sleep
    sleep(2)


from random import randint

# TODO Написать генератор, который будет генерировать указанное количество
#  псевдослучайных чисел в диапазоне от А до Б


def my_randint(a, b, count):
    for _ in range(count):
        yield randint(a, b)


# TODO Написать генератор, принимающий 3 целочисленных аргумента
#  number, start, end
#  и генерирующий число number в степени от start до end
#  number = 2, start = 3, end = 6 -> 8, 16, 32, 64


def s(start, end, number):
    for i in range(start, end + 1):
        yield number ** i


def decorator_with_arguments(a, b):
    def wrapper(func):
        def wrapped(c, d):
            c += a
            d += b
            result = func(c, d)
            print('post process')
            return result

        return wrapped
    return wrapper


@decorator_with_arguments(2, 3)
def mult(e, f):
    return e * f


header = {'Authorization': 'Bearer gcheoijjvfoiuewncyfunf89euvob3c'}


request = {
    'Headers': header,
    'body': 'Hello'
}


def is_authenticated(func):
    def wrapper(request):
        if not request.get('Headers'):
            raise ValueError('invalid headers')

        if not request.get('Headers').get('Authorization'):
            raise ValueError('invalid headers')

        if not request.get('Headers').get('Authorization').startswith('Bearer '):
            raise ValueError('invalid token type')

        return func(request)
    return wrapper


@is_authenticated
def handler(request):
    print(request.get('body'))


handler(request)
