#!/usr/bin/python3
from schema import Base
from sqlalchemy import create_engine

class CreateDB:
    
    def createData(self):
        #Declaring database location to be created and name
        DATABASE_URI = 'sqlite:///tps.db'
        engine = create_engine(DATABASE_URI, echo=False)
        #Calling Base to create database with the tables from schema
        Base.metadata.create_all(engine)

def main():
    create = CreateDB()
    create.createData()

if __name__ == "__main__":
    main()

    