from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from config import DATA_BASE_URL
Base = declarative_base()

class Dairy(Base):
    __tablename__ = 'dairy'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    

engine = create_engine(DATA_BASE_URL)
Base.metadata.create_all(bind=engine)    
