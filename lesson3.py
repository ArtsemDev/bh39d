# a = '12_34'
# a = int(a)
# b = 1_000_000_000
# c = abs(-123)


# a = '-123.3e4'
# a = float(a)
# print(a)

# a = 'inf'
# b = 'nan'
# a = float(a)
# b = float(b)
# print(a, b)

# text = 'hello\vworld\vpython\rgoodbye'
# print(text)

# hello
#      world
#           python
# text = 'hello\tworld'
# print(len(text))


# text = 'hello'
# print(text[::-1])
# print(text[-4])
# from -len to len - 1

# a = 'qwerty'
# print(a[:3] + a[3:])

# text = 'hello python world'
# hello = text[:5]
# python = text[6:12]
# world = text[13:]
# print(hello, python, world)

# name = 'Alex'
# age = 34
# text1 = 'Hello ' + name + ' your age ' + str(age)
# text2 = 'Hello %(first_name)s your age %(age)d' % {'first_name': name, 'age': age}
# text3 = 'Hello {first_name} your age {age} {age}'.format(first_name=name, age=age*2)
# text4 = f'Hello {name} your age {age*2} {age*2}'
# print(text1)
# print(text2)
# print(text3)
# print(text4)

# text = 'hello python world pycharm'
# # words = text.split('---')
# text = '|'.join(text)
# print(text)

# text = 'hello python python world'
# print(text.partition('yth'))
# print(text.rpartition('yth'))
# space_count = text.count('')
# print(space_count)
# a = text.index(' ')
# b = text.rindex(' ')
# print(a)
# print(b)

# text = 'hello java java'
# text = text.replace('', '|', 6)
# print(text)

# a = 'HELLO WORLD ß'
# print(a.lower())
# print(a.upper())
# print(a.title())
# print(a.capitalize())
# print(a.swapcase())
# print(a.casefold())
# a = a.title()
# print(a)
# print(a.istitle())
# print(a.startswith('hell', 2))
# print(a.endswith('rld'))
# print(a.isdigit())
# b = a.isalpha
# print(b())


# TODO Пользователь вводит с клавиатуры предложение из 3х слов
#  необходимо вырезать каждое слово в отдельную переменную
# text = input('Enter text: ')
# first_space = text.find(' ')
# last_space = text.rfind(' ')
# word1 = text[:first_space]
# word2 = text[first_space+1:last_space]
# word3 = text[last_space+1:]
# print(word1)
# print(word2)
# print(word3)

# text = 'hello\tworld\tpython'
# text2 = 'hi\tmr\trobot'
# print(text.expandtabs(10))
# print(text2.expandtabs(10))


# text = '-.,-/hello./././.world-,./,./'
# print(text.lstrip(',./-'))
# print(text.rstrip(',./-'))
# print(text.strip(',./-'))
# text.rsplit()


# text = 'hello world'
# print(text.removeprefix('Hell'))
# print(text.removesuffix('rld'))


# text = 'hello'
# print(text.center(10))
# print(text.ljust(10, '-'))
# print(text.rjust(10, '0'))
# print(text.zfill(10))

# print(bin(13)[2:].zfill(8))
# print('hello world мир'.encode('utf-8').decode('utf-8'))
# from math import ceil
# text = 'привет мир'
# print(ceil(len(text.encode()) / 140))


# print('\v'.isprintable())


# text = '''
# hello
# world
# '''

# text = 'hello\nworld'
# print(text.splitlines())

# text = 'hello'
# text2 = 'hello world'
# print(text > text2)


# text = 'hello world python world'
# print('world' not in text)

# a = 4
# b = 2 * 2
# print(a is b)

# print(bin(13))
# print(bin(14))
# print(bin(13 ^ 14))

# print(bin(13))
# print(~13)

# text = 'hello'
# print(text[0])
# print(text[~0])

# print((13 >> 2))
# n = int(input())

# print((n & (n - 1) == 0) and n != 0)


# text = 'Hello'
# data = {'H': 1, 'e': 1, 'l': 2, 'o': 1}

# n = 3
# data = {
#     0: {'name': 'name1', 'email': 'email1'},
#     1: {'name': 'name2', 'email': 'email2'},
#     2: {'name': 'name3', 'email': 'email3'},
# }

# letters = [i for i in 'hello world']
# print(letters)
# text = 'hello'
# data = {text[i].upper(): 12345678 for i in range(5)}
# print(data)
# n = int(input('Enter N: '))
# print(n)
