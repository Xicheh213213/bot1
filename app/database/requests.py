from app.database.models import User,Category,SubCategory,Item,Basket,async_session
from sqlalchemy import select

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
    if not user:
        session.add(User(tg_id =tg_id))
        await session.commit()

async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))
    
async def get_subcategory(category_id):
     async with async_session() as session:
         return await session.scalars(select(SubCategory).where(SubCategory.category==category_id))
     
async def get_items(subcategoty_id):
     async with async_session() as session:
         return await session.scalars(select(Item).where(Item.subcategory==subcategoty_id))
     
async def get_item(item_id):
     async with async_session() as session:
          return await session.scalar(select(Item).where(Item.id==item_id))
     
async def get_nameitem(item_name):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.name==item_name))

async def get_users():
    async with async_session() as session:
         return await session.scalars(select(User))