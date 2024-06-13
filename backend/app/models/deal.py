from sqlalchemy import String, Column, Integer, select
from app.models.base import Base, TimeStampMixin
from sqlalchemy.ext.asyncio import AsyncSession

class Deal(Base, TimeStampMixin):
    __tablename__ = 'deals'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    merchant_id = Column(Integer)
    merchant_name = Column(String)
    network = Column(String)
    network_id = Column(Integer)
    homepage_url = Column(String)
    status = Column(String)
    merchant_about = Column(String)
    
    @classmethod
    async def find_by_merchant_id(cls, db_session: AsyncSession, merchant_id: int):
        stmt = select(cls).filter_by(merchant_id=merchant_id)
        result = await db_session.execute(stmt)
        return result.scalars().first()
    
    @classmethod
    async def find_by_merchant_name(cls, db_session: AsyncSession, merchant_name: str):
        stmt = select(cls).filter_by(merchant_name=merchant_name)
        result = await db_session.execute(stmt)
        return result.scalars().first()
    
    @classmethod
    async def find_all(cls, db_session: AsyncSession):
        stmt = select(cls)
        result = await db_session.execute(stmt)
        return result.scalars().all()
    
    