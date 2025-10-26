from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Image(Base):
    __tablename__ = "images" #table anme in a database

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String, index=True)
    system_filename = Column(String,unique=True,index=True)
    file_size_bytes=Column(Integer)
    uploaded_at=Column(DateTime, default=datetime.utcnow)
