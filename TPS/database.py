#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///tps.db'

class getSession:
    
    def get_db_session(self):
        engine = create_engine(DATABASE_URI, echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session 