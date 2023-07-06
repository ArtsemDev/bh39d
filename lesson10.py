# # file = open('input.txt', 'r', encoding='utf-8')
# # file.close()
#
# # from time import sleep
# #
# # with open('input.txt', 'r', encoding='utf-8') as file:
# #     for line in file:
# #         sleep(5)
#
#
# # TODO Дан txt файл, в каждой строке файла записаны числа через запятую
# #  необходимо прочитать файл и высчитать сумму чисел в каждой строке
# #  результаты записать в новый файл
#
#
# # with open('input.txt', 'r', encoding='utf-8') as file:
# #     lines = [f'{sum(int(number) for number in line.strip().split())}\n' for line in file]
# #
# # with open('output.txt', 'w', encoding='utf-8') as file:
# #     file.writelines(lines)
#
#
# # Скобки в контекстном менеджере Python3.11+
#
# # with (
# #     open(file='input.txt', mode='r', encoding='utf-8') as file,
# #     open(file='output.txt', mode='w', encoding='utf-8') as file2
# # ):
# #     lines = [f'{sum(int(number) for number in line.strip().split())}' for line in file]
# #     file2.write('\n'.join(lines))
#
# # with open('input.txt', 'r', encoding='utf-8') as file:
# #     lines = file.readlines()
# #
# # lines[0] = 'Hello world\n'
# # with open('input.txt', 'w', encoding='utf-8') as file:
# #     file.writelines(lines)
#
# from csv import reader, DictReader, writer, DictWriter
#
#
# # with open('input.csv', 'r', encoding='utf-8') as file:
# #     # r = reader(file)
# #     # for line in r:
# #     #     print(line)
# #     r = DictReader(file, fieldnames=['name', 'email', 'age'])
# #     for line in r:
# #         print(line)
#
#
# # lines = [['vasya', 'vasya@gmail.com'], ['petya', 'petya@gmail.com']]
# # lines = [
# #     {'name': 'vasya', 'email': 'vasya@gmail.com'},
# #     {'name': 'petya', 'email': 'petya@gmail.com'},
# # ]
# # with open('output.csv', 'w', encoding='utf-8') as file:
# #     w = DictWriter(file, fieldnames=['name', 'email'])
# #     w.writeheader()
# #     w.writerows(lines)
#
# # from ujson import loads, load, dumps, dump
#
# # with open('input.json', 'r', encoding='utf-8') as file:
# #     data = load(file)
#
#
# # text = '''{
# #   "name": "Vasya",
# #   "email": "vasya@gmail.com",
# #   "is_human": true,
# #   "city": null,
# #   "languages": ["en", "ru"],
# #   "age": 23
# # }'''
# # data = loads(text)
# #
# # print(data)
#
# # data = {
# #     'name': 'Петя',
# #     'email': 'petya@gmail.com',
# #     'city': None
# # }
# # with open('output.json', 'w', encoding='utf-8') as file:
# #     dump(data, file, indent=2, ensure_ascii=False)
#
# # text = dumps(data)
# # print(text)
# from typing import Optional, List
#
# from pydantic import BaseModel, EmailStr, Field, PositiveInt, field_validator, validator
# from pydantic.types import Decimal
# from ujson import loads, dumps
#
#
# class User(BaseModel):
#     # first_name: str = Field(default='Vasya', const=True)  # firstName
#     username: str = Field(..., min_length=4, max_length=16)
#     # email: EmailStr = None
#     # email: EmailStr | None
#     email: Optional[EmailStr]
#     # email: EmailStr = Field(default=None)
#     password: str
#     languages: Optional[List[str]]
#     foo: List[int]
#     # price: Decimal = Field(max_digits=8, decimal_places=2)
#
# # user = User.parse_obj(**data)
# # user = User.parse_file()
# # user = User.construct(**data)
#
#
# class Product(BaseModel):
#     id: PositiveInt
#     title: str = Field(max_length=128)
#     price: Decimal = Field(max_digits=8, decimal_places=2)
#
#
# class Category(BaseModel):
#     id: PositiveInt
#     name: str = Field(max_length=64)
#     products: Optional[List[Product]]
#     subcategories: Optional[List['Category']]
#
#
#
# data = {
#     'id': 1,
#     'name': 'Coffee',
#     'products': [
#         {
#             'id': 1,
#             'title': 'Cappuccino',
#             'price': 5.5
#         },
#         {
#             'id': 2,
#             'title': 'Latte',
#             'price': 6
#         }
#     ],
#     'subcategories': [
#         {
#             'id': 2,
#             'name': 'Hot'
#         }
#     ]
# }
#
# cat = Category(**data)


from pydantic import BaseModel, EmailStr, field_validator, Field, model_validator


db = ['vasya@gmail.com', 'petya@gmail.com']


class User(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)

    @field_validator('email')
    def email_validate(cls, value):
        if value in db:
            raise ValueError('email is not unique')
        return value

    @model_validator(mode='before')
    def validator(cls, values):
        if values.get('username').lower() in values.get('password').lower():
            raise ValueError('password has not constraint username')
        return values


user = User(email='vasya2@gmail.com', username='Vasya', password='VAsyasdfsdf')
