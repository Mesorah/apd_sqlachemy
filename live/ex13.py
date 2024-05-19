from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    comment = Column(String, primary_key=False)
    live = Column(String, primary_key=False)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f'Comment({self.id=}, {self.name=}, {self.comment=}, {self.live=}, {self.created_at=})'
    
Comment(name='', comment='', live='')