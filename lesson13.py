# from psycopg2 import connect
# from psycopg2._psycopg import connection
# from psycopg2.extras import NamedTupleCursor
#
#
# # conn = connect(
# #     dbname='bh39d',
# #     user='learn',
# #     password='newstrongpassword',
# #     host='0.0.0.0',
# #     port='5432'
# # )
#
# # conn: connection = connect(
# #     dsn='postgresql://learn:newstrongpassword@0.0.0.0:5432/bh39d',
# #     cursor_factory=NamedTupleCursor
# # )
#
# with connect(
#     dsn='postgresql://learn:newstrongpassword@0.0.0.0:5432/bh39d',
#     cursor_factory=NamedTupleCursor
# ) as conn:  # type: connection
#     with conn.cursor() as cur:  # type: NamedTupleCursor
#         cur.execute('''
#         CREATE TABLE IF NOT EXISTS category(
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(64) NOT NULL UNIQUE
#         );
#         ''')
#         conn.commit()

from asyncio import run
from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    TEXT,
    DECIMAL,
    ForeignKey,
    create_engine,
    select,
)
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    relationship,
    sessionmaker,
    selectinload
)
from sqlalchemy.sql.functions import count


# Устаревший вариант создания базовой модели в алхимии до 2 версии
# Base = declarative_base()


# Новый вариант создания базовой модели в алхимии начиная с версии 2
class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://learn:newstrongpassword@0.0.0.0:5432/bh39d')
    session = sessionmaker(bind=engine)
    async_engine = create_async_engine('postgresql+asyncpg://learn:newstrongpassword@0.0.0.0:5432/bh39d')
    async_session = async_sessionmaker(bind=async_engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


class Category(Base):
    # обязательный атрибут указывающий на название таблицы в СУБД
    # __tablename__ = 'category'

    name = Column(VARCHAR(64), nullable=False, unique=True)  # name VARCHAR(64) NOT NULL UNIQUE
    # date_created = Column(TIMESTAMP, default=datetime.utcnow(), onupdate=datetime.utcnow())

    products = relationship('Product', back_populates='category')

    def __getitem__(self, item):
        with self.session() as session:
            obj = session.scalar(
                select(self.__class__)
                .limit(1)
                .offset(item)
            )
            if obj is None:
                raise IndexError
            else:
                return obj

    def __len__(self):
        with self.session() as session:
            return session.scalar(select(count(self.__class__.id)))


class Product(Base):
    name = Column(VARCHAR(128), nullable=False)
    descr = Column(TEXT)
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)

    category = relationship('Category', back_populates='products')

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.price >= other.price
        elif isinstance(other, int | float):
            return self.price >= other


# Base.metadata.create_all(bind=Base.engine)


# category = Category(name='Sandwich')
# with Category.session() as session:
#     session.add(category)
#     try:
#         session.commit()
#     except IntegrityError:
#         pass
#     else:
#         session.refresh(category)
#         print(category.id, category.name)

# with Category.session() as session:
#     category_1 = session.get(Category, 3)
#     session.delete(category_1)
#     session.commit()

# with Category.session() as session:
#     category_1 = session.get(Category, 1)
#     category_1.name = 'Кофе'
#     session.commit()

# with Category.session() as session:
# objs = session.execute()  # Удобен для UNION/JOIN запросов [(Category, Product), (Category, Product)]
# objs = session.scalars()  # удобен для SELECT из 1 таблицы [Category, Category]
# obj = session.scalar()  # удобен для SELECT из 1 таблицы 1 записи Category
# objs = session.scalars(
#     select(Category)
#     .filter(Category.id.in_([2]))
#     .order_by(Category.name.desc())
# )
# print(objs.all())


# with Product.session() as session:
#     # products = [
#     #     Product(
#     #         name='Product 1',
#     #         descr='Description 1',
#     #         price=55.5,
#     #         category_id=1
#     #     ),
#     #     Product(
#     #         name='Product 2',
#     #         descr='Description 2',
#     #         price=45.4,
#     #         category_id=1
#     #     )
#     # ]
#     # session.add_all(products)
#     # session.commit()
#     # products = [session.refresh(product) for product in products]
#     # cat = session.get(Category, 1)
#     # print(cat.products)
#
#     # isouter=False - INNER JOIN
#     # isouter=True - LEFT/RIGHT JOIN
#     # full=True - FULL OUTER JOIN
#     objs = session.execute(
#         select(Category, Product)
#         .join(Product, isouter=True)
#     )
#     print(objs.all())


# objs = [2, 3, 4, 2]
# print(all(objs))

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# with Product.session() as session:
#     session.execute(
#         update(Product)
#         .values(
#             price=Product.price * 0.95
#         )
#         .filter(Product.category_id == 1)
#         .order_by(Product.id.desc())
#         .limit(2)
#         .offset(3)
#     )
#     session.commit()


# with Product.session() as session:
#     session.execute(
#         delete(Product)
#         .filter(Product.price < 45)
#     )
#     session.commit()


async def main():
    async with Category.async_session() as session:
        # cat = await session.get(Category, 1, options=[selectinload(Category.products)])
        cat = await session.scalars(select(Category).options(selectinload(Category.products)))
        for c in cat:
            print(c.products)


run(main())
