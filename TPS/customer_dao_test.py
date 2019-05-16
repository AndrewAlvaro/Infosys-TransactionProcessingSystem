#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from customer_dao import CustomerDAO
from database import getSession

#Passing class to be used
dao = CustomerDAO()
#Passing session to be used
session = getSession()
    

class RunTest:

    def test_create(self):
        getSession = session.get_db_session()
        
        """
        data = {}
        data['firstname'] = "France"
        data['lastname'] = "Cheong"
        data['title'] = "Mr"
        data['email'] = "f.cheong@gmail.com"
        data['work_phone'] = "(02) 9999 9999"


        'firstname':"Andrew",
        'lastname': "Andrew",
        'email': "andrew.alvaro10@gmail.com",
        'phone_no': "0400000000",
        'dob': "21/06/1995"

        'firstname':"France",
        'lastname': "Cheong",
        'email': "f.cheong@gmail.com",
        'phone_no': "(02) 9999 9999",
        'dob': "01/01/1995"
        """
        #Data to be created in JSON format
        data = {
            'firstname':"France",
            'lastname': "Cheong",
            'email': "f.cheong@gmail.com",
            'phone_no': "(02) 9999 9999",
            'dob': "01/01/1995"
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
        customer_id = input("Enter customer ID: ") 

        #Calling function from customer_dao finding customer by ID passing session and customer ID input
        result = dao.find_by_id(getSession, customer_id)
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

    def test_find_by_lastname(self):
        getSession = session.get_db_session()
        
        #Asking user to input the lastname of customer search for
        lastname = input("Please input the lastname: ")

        #Calling function from customer_dao passing session and lastname 
        result = dao.find_by_lastname(getSession, lastname)
        #Printing result of customer that is found by the lastname
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
        customer_id = input("Enter customer ID: ") 

        #Information to be updated in JSON format
        data = {}
        data['firstname'] = "France"
        data['lastname'] = "James"
        data['email'] = "j.James@gmail.com"
        data['phone_no'] = "(02) 8888 9995"
        data['dob'] = "01/01/1996"
        
        #Calling function from customer_dao passing session, customer_id selected and the data to be updated
        result = dao.update(getSession, customer_id, data)
        #Printing result of the customer information updated
        print(result)

        #Closing the session between database
        getSession.close()    

    def test_delete(self):
        getSession = session.get_db_session()

        #Asking user to input customer ID to be deleted
        customer_id = input("Enter customer ID: ") 

        #Calling function from customer_dao pasing session and customer_id to be deleted
        result = dao.delete(getSession, customer_id)

        # Print the result
        print(result)

        # Close the session
        getSession.close()          

#Main menu
def main():
    run = RunTest()

    print("------Main menu------\n 1. Create new customer\n 2. Find customer by ID\n 3. Display all customer\n 4. Update existing customer details\n 5. Find customer by lastname\n 6. Display all customer IDs\n 7. Delete customer details")  
  
    
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
            run.test_find_by_lastname()
            return True
        
        if(option == '6'):    
            run.test_find_ids()
            return True

        if(option == '7'):    
            run.test_delete()
            return True
          
        else:
            print("Command not found!")
            return False
if __name__ == '__main__':
    main()