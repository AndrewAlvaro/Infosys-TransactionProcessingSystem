from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from schema import Movie
from schema import Customer
from schema import Screening

from database import getSession

class PopulateTable:

    def populate(self, session):

        session.add_all([
            Customer(
                    customer_id = '1',
                    firstname = 'George', 
                    lastname = 'Tanner', 
                    email = 'george.tanner@gmail.com',
                    phone_no = '98120001',
                    dob ='25/07/1993'),

            Customer(
                    customer_id = '2',
                    firstname = 'Samantha', 
                    lastname = 'Riley', 
                    email = 'samantha.riley@gmail.com',
                    phone_no = '98120002',
                    dob ='15/03/1987'),

            Customer(
                    customer_id = '3',
                    firstname = 'Rebecca', 
                    lastname = 'White', 
                    email = 'rebecca.white@gmail.com',
                    phone_no ='98120003',    
                    dob = '07/11/1995'),
            ])

        session.add_all([
            Movie(
                movie_id='4125', 
                movie_name='Avengers: Endgame', 
                ratings='M'),

            Movie( 
                movie_id='4128', 
                movie_name='Pet Semetary', 
                ratings='R18+'),

            Movie(
                movie_id='4130', 
                movie_name='Star Wars: The rise of Skywalker', 
                ratings='M'),
        ])


def main():
    getSessionnow = getSession()
    populate = PopulateTable()
    
    session = getSessionnow.get_db_session()
    
    populate.populate(session)

    session.commit()
    session.close()

if __name__ == "__main__":
       main()
