#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movie_dao import MovieDAO
from database import getSession

#Passing class to be used
dao = MovieDAO()
#Passing session to be used
session = getSession()
    

class RunTest:

    def test_create(self):
        getSession = session.get_db_session()
        
        #Data to be created in JSON format
        data = {
            'movie_name':"Pokemon",
            'ratings': "G",
        }

        
        #Calling function from customer_dao create passing session and data through
        result = dao.create(getSession, data)
        #Printing the result of the data created
        print(result)
       
        #Closing the session between database
        getSession.close()

    def test_find_by_id(self):
        getSession = session.get_db_session()
        #Asking user to input customer ID to find
        movie_id = input("Enter movie ID: ") 

        #Calling function from customer_dao finding customer by ID passing session and customer ID input
        result = dao.find_by_id(getSession, movie_id)
        #Printing result of the customer information is found 
        print(result)

        #Closing the session between database
        getSession.close()

    def test_find_all(self):
        getSession = session.get_db_session()

        #Calling function from customer_dao showing all customer in database 
        result = dao.find_all(getSession)
        #Printing result of all customer in database
        print(result)

        #Closing the session between database
        getSession.close()    


    def test_find_ids(self):
        getSession = session.get_db_session()
        
        #Calling function from customer_dao passing session showing all customer IDs
        result = dao.find_ids(getSession)
        #Printing result of customer IDs
        print(result)

        #Closing the session between database
        getSession.close()    

    def test_update(self):
        getSession = session.get_db_session()

        #Asking user to input customer ID to update information
        movie_id = input("Enter movie ID: ") 

        #Information to be updated in JSON format
        data = {}
        data['movie_name'] = "Pokemon"
        data['ratings'] = "G"
        
        #Calling function from customer_dao passing session, customer_id selected and the data to be updated
        result = dao.update(getSession, movie_id, data)
        #Printing result of the customer information updated
        print(result)

        #Closing the session between database
        getSession.close()    

    def test_delete(self):
        getSession = session.get_db_session()

        #Asking user to input customer ID to be deleted
        movie_id = input("Enter movie ID: ") 

        #Calling function from customer_dao pasing session and customer_id to be deleted
        result = dao.delete(getSession, movie_id)

        # Print the result
        print(result)

        # Close the session
        getSession.close()          

#Main menu
def main():
    run = RunTest()

    print("------Main menu------\n 1. Insert new movie\n 2. Find movie by ID\n 3. Display all movie\n 4. Update existing movie details\n 5. Display all customer IDs\n 6. Delete customer details")  
  
    
    while True:
        option = input("Please select the following options: ")
        
        if(option == '1'):
            run.test_create()
            return True
            
        if(option == '2'):
            run.test_find_by_id()
            return True

        if(option == '3'):
            run.test_find_all()
            return True

        if(option == '4'):
            run.test_update()
            return True

        if(option == '5'):    
            run.test_find_ids()
            return True

        if(option == '6'):    
            run.test_delete()
            return True
          
        else:
            print("Command not found!")
            return False
if __name__ == '__main__':
    main()