#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from schema import Movie
from schema import Customer
from schema import Screening
from schema import Ticket
from schema import Booking
from database import getSession

class PopulateTable:

    def populate(self, session):
        #Populating database with information 
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
        session.add_all([
            #Avenegers: Endgame session time
            Screening(
                cinema_id='1',
                movie_id='4125', 
                cinema_no='6', 
                session_date='24/04/2019',
                session_time='18:00'),

            Screening(
                cinema_id='2',
                movie_id='4125', 
                cinema_no='6', 
                session_date='24/04/2019',
                session_time='18:00'),
            
            Screening(
                cinema_id='3',
                movie_id='4125', 
                cinema_no='6', 
                session_date='24/04/2019',
                session_time='18:00'),

            Screening(
                cinema_id='4',
                movie_id='4125', 
                cinema_no='6', 
                session_date='24/04/2019',
                session_time='18:00'),
            
            Screening(
                cinema_id='5',
                movie_id='4125', 
                cinema_no='6', 
                session_date='24/04/2019',
                session_time='18:00'),
            #Pet Sematary session time
            Screening( 
                cinema_id='6',
                movie_id='4128', 
                cinema_no='2', 
                session_date='24/04/2019',
                session_time='18:00'),

            #Star Wars: The rise of Skywalker session time
            Screening(
                cinema_id='7',
                movie_id='4130', 
                cinema_no='10', 
                session_date='24/04/2019',
                session_time='18:00'),

        ])

        session.add_all([
            Ticket(
                ticket_id='1',
                cinema_id='5'), 

            Ticket(
                ticket_id='2',
                cinema_id='6'), 

            Ticket(
                ticket_id='3',
                cinema_id='7'), 
        ])
        
        session.add_all([
            Booking(
                booking_id='1',
                customer_id='1',
                ticket_id='1',
                booking_date='01/04/2019',
                num_guests='1',
                comment=' '), 

            Booking(
                booking_id='2',
                customer_id='2',
                ticket_id='2',
                booking_date='02/04/2019',
                num_guests='1',
                comment=' '), 

            Booking(
                booking_id='3',
                customer_id='3',
                ticket_id='3',
                booking_date='03/04/2019',
                num_guests='1',
                comment=' '), 
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
