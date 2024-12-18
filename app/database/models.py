from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncAttrs
import os
from sqlalchemy import BigInteger,String,ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(url = os.getenv('SQLALCHEMY_URL'))

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs,DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id:Mapped[int]=mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

class Category(Base):
    __tablename__ = 'categories'

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(25))

class SubCategory(Base):
    __tablename__ = 'subcategories'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(30))
    category:Mapped[int]=mapped_column(ForeignKey('categories.id'))

class Item(Base):
    __tablename__='items'

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(30))
    descripion:Mapped[str]=mapped_column(String(128))
    price:Mapped[str]=mapped_column(String(10))
    subcategory: Mapped[int]=mapped_column(ForeignKey('subcategories.id'))

class Basket(Base):
    __tablename__ = 'basket'

    id:Mapped[int]=mapped_column(primary_key=True)
    user:Mapped[int]=mapped_column(ForeignKey('users.id'))
    item:Mapped[int]=mapped_column(ForeignKey('items.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)