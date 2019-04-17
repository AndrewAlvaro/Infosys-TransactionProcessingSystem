
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship 


Base = declarative_base()


class Customer(Base): 

    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True) # primary key
    firstname = Column(String(255), nullable=False) # non null
    lastname = Column(String(255), nullable=False) # non null
    email = Column(String(255), nullable=False, unique=True)
    phone_no = Column(Integer, nullable=False, unique=True) # non null, unique
    dob = Column(String(255), nullable=False, unique=True) # non null, unique
    pass

class Booking(Base):

    __tablename__ = 'booking'

    booking_id = Column(Integer, primary_key=True) # primary key
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    ticket_id = Column(Integer, ForeignKey("ticket.ticket_id"))
    booking_date = Column(String(10), nullable=False)
    num_guests = Column(Integer, nullable=False)
    comment = Column(String(255), nullable=True)
    

class Movie(Base):

    __tablename__ = 'movie' # i.e. supplier (all lower case, singular)

    movie_id = Column(Integer, primary_key=True) # primary key
    movie_name = Column(String(255), nullable=False)
    ratings = Column(String(5), nullable=False)
    

class Screening(Base):

    __tablename__ = 'screening' 

    cinema_id = Column(Integer, primary_key=True) # primary key
    movie_id = Column(Integer, ForeignKey("movie.movie_id")) # foreign key
    cinema_no = Column(Integer, nullable=False) 
    session_time = Column(Date, nullable=False)
    session_date = Column(Date, nullable=False)

class Ticket(Base):

    __tablename__ = 'ticket' 

    ticket_id = Column(Integer, primary_key=True) # Primary key
    cinema_id = Column(Integer, ForeignKey("screening.cinema_id")) # Foreign key
  