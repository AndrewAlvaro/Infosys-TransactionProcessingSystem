#!/usr/bin/env python3
from schema import Customer


class CustomerDAO:
    

    def create(self, session, data):
        print("\nCreating new customer...")
        #Printing data passed from customer_dao_test
        print(data)

        #Passing data into customer table
        customer = Customer(firstname = data['firstname'], 
                            lastname = data['lastname'], 
                            email = data['email'], 
                            phone_no = data['phone_no'],
                            dob = data['dob'])

        #Adding the data into the table
        session.add(customer)
        #Commiting the session
        session.commit() 

        #Creating empty dict
        result = {}  
        #Store an appropriate message in the result dict under key "message"
        result['message'] = 'Customer added successfully!'

        inserted_customer_id = customer.customer_id
        #Store customer_id in the result dict under key "customer_id"
        result['customer_id'] = inserted_customer_id

        #Returning the dict result
        return result

    def find_by_id(self, session, customer_id):
        print("\nFinding a customer by ID...")
        #Printing the customer_id passed in from customer_dao_test
        print(customer_id)

        #Getting the customer id from Customer table
        customer = session.query(Customer).get(customer_id)
        
        #Creating empty dict
        result = {}

        #If statement: if customer not found store message
        if not customer:
            result['message'] = "Customer NOT found"
        
        #Else statement: else if customer is found display the customer information
        else:
            display = {} 
            display['customer_id'] = customer.customer_id
            display['firstname'] = customer.firstname
            display['lastname'] = customer.lastname
            display['email'] = customer.email
            display['phone_no'] = customer.phone_no
            display['dob'] = customer.dob
            
            result['customer'] = display
        
        #Returning result
        return result

    def find_all(self, session):
        print("Finding all customers ...")

        #Creating empty dict
        result = {}

        #Getting all customer exists in Customer table
        rows = session.query(Customer).all()

        #If statement: if no customer is found store message
        if not rows:
            result['message'] = "No customers found!"
        
        #Else statement: else if customer(s) is found display all the customer in Customer table
        else:
            list_customer = [] 
            for x in rows:
                display = {}
                display['customer_id'] = x.customer_id
                display['firstname'] = x.firstname
                display['lastname'] = x.lastname
                display['email'] = x.email
                display['phone_no'] = x.phone_no
    
                list_customer.append(display)
                pass    
           
            result['customer'] = list_customer

        #Returning result
        return result 

    def update(self, session, customer_id, data):
        print("Updating customer details ...")
        #Printing the customer_id passed in from customer_dao_test
        print(customer_id)
        #Printing the data passed in from customer_dao_test
        print(data)

        #Creating empty dict
        result = {}

        #Getting customer_id from database if exists
        customer = session.query(Customer).get(customer_id)

        #If statement: if customer exists update the following customer information
        if customer:
            customer.fistname = data['firstname']
            customer.lastname = data['lastname']
            customer.email = data['email']
            customer.phone_no = data['phone_no']
            customer.dob = data['dob']
            
            session.commit() 

            result['message'] = "Customer details updated!"     
        
        #Else statement: else if customer doesn't exists store message
        else:
            result['message'] = "Customer not found!"

        #Returning result
        return result

    def delete(self, session, customer_id):
        print("\nDeleting customer details...")
        #Printing the customer_id passed in from customer_dao_test
        print(customer_id)

        #Creating empty dict
        result = {}

        #Getting customer_id from database if exists
        customer = session.query(Customer).get(customer_id)

        #If statement: if customer is found delete customer
        if customer:
            session.delete(customer)          
            session.commit()
      
            result['message'] = "Customer deleted"  

        #Else statement: else if customer is not found store message
        else:  
            result['message'] = "Customer not found"

        #Return result
        return result

    def find_by_lastname(self, session, lastname):
        print("\nFind a customer by lastname...")
        
        #Print lastname passed in from customer_dao_test
        print(lastname)

        #Create empty dict
        result = {}

        #Looking through database Customer table filtering by lastname given and showing all the customer with the lastname
        rows = session.query(Customer) \
            .filter(Customer.lastname.like(lastname)) \
            .order_by(Customer.customer_id).all()   

        #If statement: if customer doesn't exist store message
        if not rows:
            result['message'] = "Customer NOT found"
        
        #Else statement: else if customer exist store the customer information in result
        else:
            list_customer = []
            for customer in rows:
                display = {} 
                display['customer_id'] = customer.customer_id
                display['firstname'] = customer.firstname
                display['lastname'] = customer.lastname
                display['email'] = customer.email
                display['phone_no'] = customer.phone_no
                
                list_customer.append(display)

            result['customer'] = display
        
        #Return result
        return result

    def find_ids(self, session):
        print("\nDisplaying all customer ID...")
        print("\nFinding all employee ids ...")
        
        #Create empty dict
        result = {}

        #Getting all customer infromation from Customer table
        rows = session.query(Customer).all()

        #If statement: if no customer exists store message
        if not rows:
            result['message'] = "No customer found!"
        
        #Else statement: else if customer exists in Customer table print customer(s) IDs
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.customer_id)
                pass               

            result['customer_ids'] = list_ids
        
        #Return result
        return result
