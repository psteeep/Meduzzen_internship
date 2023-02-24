from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql.functions import func
from app.connect_db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String)
