from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.model import Dairy
from config import DATA_BASE_URL



class Database:
    engine = create_engine(DATA_BASE_URL)
    Session = sessionmaker(bind=engine)
  

    def __init__(self):
        self.session = Database.Session()

    def AddToDB(self, name, description): 
        dairy = Dairy(name=name, description=description)
        self.session.add(dairy)
        self.session.commit()
        
    def get_data(self):
        return self.session.query(Dairy).all()

    def PrintAllTaskFromDb(self):
        dairies = self.session.query(Dairy).all()
        for dairy in dairies:
            print(dairy.name, dairy.description)
            
    def DeleteTaskFromDb():
        _name = input("Enter the name of the task you want to delete\t")
        session.query(Dairy).filter(Dairy.name == _name).delete()
        session.commit()
        
