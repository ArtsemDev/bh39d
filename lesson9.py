class User(object):

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f'User: username={self.username}'

    def change_password(self, new_password):
        if len(new_password) < 8 or len(new_password) > 64:
            raise ValueError
        self.password = new_password


class Manager(User):

    def __init__(self, username: str, password: str):
        super().__init__(username, f'{username.lower()}@gmail.com', password)
        self.salary = 1500

    def __str__(self):
        data = super().__str__()
        return data + f' email={self.email}'


class A:
    pass


class B:

    def __init__(self, b):
        self.b = b


class C(A, B):
    pass


from abc import ABC, abstractmethod


class Music(ABC):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    @abstractmethod
    def get(cls, name: str) -> str:
        pass


class YandexMusic(Music):

    @classmethod
    def get(cls, name: str) -> str:
        return f'Yandex: {name}'


class Spotify(Music):

    @classmethod
    def get(cls, name: str) -> str:
        return f'Spotify: {name}'


class Client:

    def __init__(self, token: str):
        self.__token = token

    @property
    def token(self):
        return self.__token[:5]

    @token.setter
    def token(self, value):
        if not isinstance(value, str):
            raise TypeError

        if len(value) < 8:
            raise ValueError

        self.__token = value


# SOLID
# S - Single Responsibility
# O - Open/Closed
# L - Liskov
# I - Interface Segregation
# D - Dependency Inversion


class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def drink(self):
        pass


class LandAnimal(ABC):

    @abstractmethod
    def run(self):
        pass


class AmphibiousAnimal(ABC):

    @abstractmethod
    def swim(self):
        pass


class Fish(Animal, AmphibiousAnimal):

    def swim(self):
        pass

    def drink(self):
        pass

    def eat(self):
        pass


class Cat(Animal, LandAnimal):

    def run(self):
        pass

    def drink(self):
        pass

    def eat(self):
        pass


class Frog(Animal, AmphibiousAnimal, LandAnimal):

    def swim(self):
        pass

    def run(self):
        pass

    def drink(self):
        pass

    def eat(self):
        pass


class AbstractStreaming(ABC):

    @abstractmethod
    def get(self, name) -> str:
        pass


class Streaming1(AbstractStreaming):

    def get(self, name) -> str:
        pass


class Streaming2(AbstractStreaming):

    def get(self, name) -> str:
        pass


class Streaming(AbstractStreaming):

    def get(self, name, streaming: Streaming1 | Streaming2) -> str:
        return streaming.get(name=name)


# YAGNI
# KISS

# from pydantic import BaseModel
#
#
# class UserSchema(BaseModel):
#     name: str
#     email: str
#     age: int
#
#


def info(self):
    print(self.name)


# Person = type('Person', (), {'name': None, 'info': info})
# vasya = Person()
# vasya.name = 'Vasya'
# vasya.info()

class Singleton(type):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            obj = type(cls.__name__, *args, **kwargs)
            cls._instance = obj
            return obj
        return cls._instance


class MySingleton(Singleton):
    pass
