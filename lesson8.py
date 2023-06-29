class User:
    role = 'user'  # атрибут класса
    # __name__ = 'User'

    def __init__(self, first_name, email, age):
        """Конструктор пользователя

        :param first_name: Имя пользователя
        :param email: почта пользователя
        :param age: возраст пользователя
        """
        self.name = first_name.title()
        self.email = email
        self.is_active = True
        self.age = age
        self.i = -1

    def block(self) -> None:
        """Блокировка пользователя"""
        self.is_active = False

    @classmethod
    def from_dict(cls, data) -> "User":
        return cls(first_name=data.get('first_name'), email=data.get('email'))
#
#     @staticmethod
#     def foo():
#         print('foo')
#
#     def __str__(self):
#         return f'User: name={self.name} email={self.email} is_active={self.is_active}'
#
#     def __bool__(self):
#         return self.is_active
#
#     def __gt__(self, other):  # >
#         if isinstance(other, User):
#             return self.age > other.age
#         elif isinstance(other, int):
#             return self.age > other
#         else:
#             raise TypeError
#
#     def __ge__(self, other):
#         if isinstance(other, User):
#             return self.age >= other.age
#         elif isinstance(other, int):
#             return self.age >= other
#         else:
#             raise TypeError
#
#     def __lt__(self, other):
#         return not self.__ge__(other)
#
#     def __le__(self, other):
#         return not self.__gt__(other)
#
#     def __eq__(self, other):
#         if isinstance(other, User):
#             return self.age == other.age
#         elif isinstance(other, int):
#             return self.age == other
#         else:
#             raise TypeError
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __getitem__(self, item):
#         return getattr(self, item)
#
#     def __setitem__(self, key, value):
#         return setattr(self, key, value)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         try:
#             return self.name[self.i]
#         except IndexError:
#             self.i = -1
#             raise StopIteration
#
#
# user_1 = User(first_name='Vasya', email='vasya@gmail.com', age=23)
# user_2 = User(first_name='Petya', email='petya@gmail.com', age=34)
# print(list(user_1))
# # for i in user_2:
# #     print(i)
# # print(user_1['name'])
# # user_1['name'] = 'Vasek'
# # print(user_1.name)
# # print(user_1 <= 12)
# # print(setattr())
# # print(getattr(user_1, 'name'))
# # user_3 = User.from_dict({'first_name': 'Maksim', 'age': 23})
# # user_3.block()
# # print(bool(user_3))
# # if user_3:
# #     print('user is not blocked')
# # user_1.block()
# # print(user_1.is_active)
# # print(user_2.is_active)
# # print(User.__name__)
# # Не правильно
# # user_1.role = 'admin'
# # print(user_2.role)
#
# # изменение атрибута класса происходит путем обращения к нему через класс, а не объект
# # данного класса
# # user_1.__class__.role = 'admin'
# # User.role = 'admin'
# # print(user_1.role)
# # print(user_2.role)
# # vasya.name = 'Vasya'
# # print(user_1.name)
# # print(user_2.name)
# #
# # print(user_2.name, user_2.email)
# # print(user_2.__dict__)
#
#
# class Manager:
#
#     def __init__(self, salary, user=None):
#         if user is not None and isinstance(user, User):
#             self.name = user.name
#             self.email = user.email
#         else:
#             self.name = None
#             self.email = None
#         self.salary = salary
#
#
# # user_1 = Manager(1500, user_1)
# # print(type(user_1))
# # print(user_1.__dict__)


# TODO Реализовать класс DicrReader
#  конструктор класса (__init__) принимает строку в формате и записывает данную строку
#  в атрибут объекта
# data = '''name,email,age
# vasya,vasya@gmail.com,23
# petya,petya@gmail.com,34'''
# TODO необходимо реализовать метод объекта to_dict
#  приводящий данную строку к списку словарей
# d = [
#     {'name': 'vasya', 'email': 'vasya@gmail.com', 'age': '23'},
#     {'name': 'petya', 'email': 'petya@gmail.com', 'age': '34'},
# ]


class DictReader:

    def __init__(self, data):
        self.data = self.to_dict(data)
        self.iter_data = None
        # self.data = self.to_dict()

    @classmethod
    def to_dict(cls, data):
        data = [line.split(',') for line in data.split('\n')]
        # result = []
        # keys = data[0]
        # values = data[1:]
        # for value in values:
        #     result.append(dict(zip(keys, value)))
        # return result
        return [dict(zip(data[0], value)) for value in data[1:]]

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_data is None:
            self.iter_data = iter(self.data)
        return next(self.iter_data)

    def __len__(self):
        return len(self.data)


data = '''name,email,age
vasya,vasya@gmail.com,23
petya,petya@gmail.com,34'''
# print(DictReader.to_dict(data))
# reader = DictReader(data)
# print(len(reader))
# for i in reader:
#     print(i)
# print(reader[0])
# print(reader.data)
# print(reader.to_dict())
# data = [line.split(',') for line in data.split('\n')]
# data = [dict(zip(data[0], value)) for value in data[1:]]


from typing import Union, List, Dict, Tuple, Any, AnyStr, Optional


# numbers: List[int] = [1, 2, 3, 4, 5, 6]
# data: Dict[str, Any]
# new_numbers: list[int | float] | None
# old_numbers: Optional[List[Union[int, float]]]

def is_palindrome(text: AnyStr) -> bool:
    """Проверка строки на палиндром

    :param text: Строка для проверки на палиндром
    :return: True - если строка палиндром, False - в противном случае
    """
    text = text.lower()
    return text == text[::-1]


# print(is_palindrome('1234567'))

# print(is_palindrome.__doc__)

# numbers = [1, 2, 3, 4, 5, ]
#
#
# def foo(list_of_numbers: List):
#     for i in list_of_numbers:  # type i: int
#         print(i)
