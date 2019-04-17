from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///tps.db'
# File app.db will be created in the folder where the python script is found

class getSession:
    
    def get_db_session(self):
        engine = create_engine(DATABASE_URI, echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session 