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


from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    TIMESTAMP,
    TEXT,
    DECIMAL,
    ForeignKey,
    create_engine,
    select,
    update,
    delete
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import (
    declarative_base,
    DeclarativeBase,
    declared_attr,
    relationship,
    sessionmaker
)

# Устаревший вариант создания базовой модели в алхимии до 2 версии
# Base = declarative_base()


# Новый вариант создания базовой модели в алхимии начиная с версии 2
class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://learn:newstrongpassword@0.0.0.0:5432/bh39d')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


class Category(Base):
    # обязательный атрибут указывающий на название таблицы в СУБД
    # __tablename__ = 'category'

    name = Column(VARCHAR(64), nullable=False, unique=True)  # name VARCHAR(64) NOT NULL UNIQUE
    # date_created = Column(TIMESTAMP, default=datetime.utcnow(), onupdate=datetime.utcnow())

    products = relationship('Product', back_populates='category')


class Product(Base):
    name = Column(VARCHAR(128), nullable=False)
    descr = Column(TEXT)
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)

    category = relationship('Category', back_populates='products')


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

with Category.session() as session:
    # objs = session.execute()  # Удобен для UNION/JOIN запросов [(Category, Product), (Category, Product)]
    # objs = session.scalars()  # удобен для SELECT из 1 таблицы [Category, Category]
    # obj = session.scalar()  # удобен для SELECT из 1 таблицы 1 записи Category
    objs = session.scalars(
        select(Category)
        .filter(Category.id.in_([2]))
        .order_by(Category.name.desc())
    )
    print(objs.all())
