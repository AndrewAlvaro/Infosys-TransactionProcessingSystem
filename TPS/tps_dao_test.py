#!/usr/bin/env python3
from tps_dao import Alter
from database import getSession

class RunAlter:
    modify = Alter()
    session = getSession()
    
    def test_create(self):
        session = get_db_session()
        
        # Instantiate the employee DAO
        emp = EmployeeDAO()

        # Setup the data as a dictionary
        """
        data = {}
        data['firstname'] = "France"
        data['lastname'] = "Cheong"
        data['title'] = "Mr"
        data['email'] = "f.cheong@gmail.com"
        data['work_phone'] = "(02) 9999 9999"
        """

        # Alternatively, the data could be set up in JSON format
        data = {
            'firstname':"France",
            'lastname': "Cheong",
            'email': "f.cheong@gmail.com",
            'phone_no': "(02) 9999 9999" # no comma on last item
        }

        # Call the create() method from the DAO
        # and pass the dictionary as parameter
        result = emp.create(session, data)

        # Print the result
        print(result)

        # Close the session
        session.close()

    def test_find_by_id(self):
        # Get a session
        session = get_db_session()
        
        # Instantiate the employee DAO
        emp = EmployeeDAO()

        # Assign an employee_id
        employee_id = 1 # exists
        #employee_id = 2 # does not exist?
        
        # Call the find_by_id() method from the DAO
        # and pass the employee_id as parameter - could pass it directly
        result = emp.find_by_id(session, employee_id)

        # Print the result
        print(result)
        
        # Close the session
        session.close()

    def test_find_all(self):
        # Get a session
        session = get_db_session()
        
        # Instantiate the employee DAO
        emp = EmployeeDAO()

        # Call the find_all() method from the DAO
        result = emp.find_all(session)

        # Print the result
        print(result)

        # Close the session
        session.close()    

    def test_find_by_lastname(self):
        # Get a session
        session = get_db_session()
            
        # Instantiate the employee DAO    
        emp = EmployeeDAO()
        
        # Assign a lastname  
        lastname = "cheong" # exists
        #lastname = "xyz" # does not exist

        # Call the find_by_lastname() method from the DAO
        # and pass the lastname as parameter - could pass it directly
        result = emp.find_by_lastname(session, lastname)

        # Print the result
        print(result)

        # Close the session
        session.close()  

    def test_find_ids(self):
        # Get a session
        session = get_db_session()
        
        # Instantiate the employee DAO
        emp = EmployeeDAO()

        # Call the find_ids() method from the DAO
        result = emp.find_ids(session)

        # Print the result
        print(result)

        # Close the session
        session.close()    

    def test_update(self):
        # Get a session
        session = get_db_session()

        # Instantiate the employee DAO
        emp = EmployeeDAO()

        # Assign an employee_id 
        employee_id = 1 # exists
        #employee_id = 2 # does not exist?

        # Create a dictionary and add items
        # Do not add the employee_id to the dict
        data = {}
        data['firstname'] = "Joe"
        data['lastname'] = "cheong"
        data['email'] = "j.cheong@gmail.com"
        data['phone_no'] = "(02) 8888 9999"
        # Alternatively, the data could be defined in JSON format
            
        # Call the update() method from the DAO
        # and pass the employee_id and data as parameters    
        result = emp.update(session, employee_id, data)

        # Print the result
        print(result)

        # Close the session
        session.close()    

    def test_delete(self):
        # Get a session
        session = get_db_session()
            
        emp = EmployeeDAO()

        # Assign an employee_id
        employee_id = 1 # exists
        #employee_id = 2 # does not exist?

        # Call the delete() method from the DAO
        # and pass the employee_id as parameter - could pass it directly
        result = emp.delete(session, employee_id)

        # Print the result
        print(result)

        # Close the session
        session.close()          
    
def main():
    run = RunAlter()
    run.run()

    print("------Main menu------\n 1. Create new customer\n 2. Find customer by ID\n 3. Display all customer\n 4. Update existing customer details\n 5. Delete customer details")  
    option = input("Please select the following options: ")

    if(option == 1):
        modify.create(session, )
    if(option == 2):
        modify.find_by_id()
    if(option == 3):
        modify.find_all()
    if(option == 4):
        modify.update()
    if(option == 5):    
        modify.delete()

    else:
        print("Command not found!")

if __name__ == '__main__':
    main()