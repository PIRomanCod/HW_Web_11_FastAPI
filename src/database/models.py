from sqlalchemy.types import Boolean, Integer, String, DateTime, Date
from sqlalchemy import Column, func, event
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50), index=True)
    lastname = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)
    phone = Column(String(15), unique=True, index=True)
    birthday = Column(Date, nullable=True)
    additional_info = Column(String(150), default="")
    is_favorite = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


@event.listens_for(Contact, 'before_insert')
def updated_favorite(mapper, conn, target):
    if target.firstname.startswith('My'):
        target.is_favorite = True


@event.listens_for(Contact, 'before_update')
def updated_favorite(mapper, conn, target):
    if target.firstname.startswith('My'):
        target.is_favorite = True
