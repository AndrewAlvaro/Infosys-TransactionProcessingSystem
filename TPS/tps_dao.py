#!/usr/bin/env python3
from database import getSession
from schema import Customer

class Alter:
    
    def create(self, session, data):
        print("\nCreating new customer...")
        print(data)

        customer = Customer(firstname = data['firstname'], 
                    lastname = data['lastname'], 
                    email = data['email'], 
                    phone_no = data['phone_no'],
                    dob = data['dob'],
                    )
  
        session.add(customer)
        session.commit() 

        result = {}  
        result['message'] = 'Customer added successfully!'
        inserted_customer_id = customer.customer_id
        result['customer_id'] = inserted_customer_id

        return result

    def find_by_id(self, session, customer_id):

        print("\nFinding a customer ...")
        print(customer_id)
  
        customer = session.query(Customer).get(customer_id)
        
        result = {}

        if not customer:
            result['message'] = "Customer NOT found"
        else:
            display = {} 
            display['customer_id'] = customer.customer_id
            display['firstname'] = customer.firstname
            display['lastname'] = customer.lastname
            display['email'] = customer.email
            display['phone_no'] = customer.phone_no
            
            result['customer'] = customer
     
        return result

    def find_all(self, session, customer_id):
        
        # Print info for debugging
        print("Finding all customers ...")

        # Create a blank dictionary to return the result
        result = {}

        # Get the session to query the Product class and get all (may wish to sort)
        rows = session.query(Customer).all()

        if not rows:
            result['message'] = "No products found!"
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

        return result 

    def update(self, session, data, customer_id):
        print("Updating product ...")
        print(customer_id)
        print(data)

        result = {}

        customer = session.query(Customer).get(customer_id)

 
        if customer:
            customer.fistname = data['firstname']
            customer.lastname = data['lastname']
            customer.email = data['email']
            customer.phone_no = data['phone_no']
            
            session.commit() 

            result['message'] = "Customer details updated!"     
        else:
            result['message'] = "Customer not found!"

        return result

    def delete(self, session, customer_id):
        print("\nDeleting Product ...")
        print(customer_id)
 
        result = {}

        customer = session.query(Customer).get(customer_id)

        if customer:
            session.delete(customer)          
            session.commit()
      
            result['message'] = "Customer deleted"  
        else:  
            result['message'] = "Customer not found"

        return result