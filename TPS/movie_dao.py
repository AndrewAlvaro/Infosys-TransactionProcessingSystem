#!/usr/bin/env python3
from schema import Movie


class MovieDAO:
    

    def create(self, session, data):
        print("\nInserting new movie...")
        #Printing data passed from customer_dao_test
        print(data)

        #Passing data into customer table
        movie = Movie(movie_name = data['movie_name'], 
                        ratings = data['ratings'])
                        

        #Adding the data into the table
        session.add(movie)
        #Commiting the session
        session.commit() 

        #Creating empty dict
        result = {}  
        #Store an appropriate message in the result dict under key "message"
        result['message'] = 'New movie added successfully!'

        inserted_movie_id = movie.movie_id
        #Store customer_id in the result dict under key "customer_id"
        result['movie_id'] = inserted_movie_id

        #Returning the dict result
        return result

    def find_by_id(self, session, movie_id):
        print("\nFinding a customer by ID...")
        #Printing the customer_id passed in from customer_dao_test
        print(movie_id)

        #Getting the customer id from Customer table
        movie = session.query(Movie).get(movie_id)
        
        #Creating empty dict
        result = {}

        #If statement: if customer not found store message
        if not movie:
            result['message'] = "Customer NOT found"
        
        #Else statement: else if customer is found display the customer information
        else:
            display = {} 
            display['movie_id'] = movie.movie_id
            display['movie_name'] = movie.movie_name
            display['ratings'] = movie.ratings
            
            result['movie'] = display
        
        #Returning result
        return result

    def find_all(self, session):
        print("Finding all movies ...")

        #Creating empty dict
        result = {}

        #Getting all customer exists in Customer table
        rows = session.query(Movie).all()

        #If statement: if no customer is found store message
        if not rows:
            result['message'] = "No movie found!"
        
        #Else statement: else if customer(s) is found display all the customer in Customer table
        else:
            list_movie = [] 
            for x in rows:
                display = {}
                display['movie_id'] = x.movie_id
                display['movie_name'] = x.movie_name
                display['ratings'] = x.ratings
    
                list_movie.append(display)
                pass    
           
            result['movie'] = list_movie

        #Returning result
        return result 

    def update(self, session, movie_id, data):
        print("Updating movie details ...")
        #Printing the customer_id passed in from customer_dao_test
        print(movie_id)
        #Printing the data passed in from customer_dao_test
        print(data)

        #Creating empty dict
        result = {}

        #Getting customer_id from database if exists
        movie = session.query(Movie).get(movie_id)

        #If statement: if customer exists update the following customer information
        if movie:
            movie.movie_name = data['movie_name']
            movie.ratings = data['ratings']
            
            session.commit() 

            result['message'] = "Movie details updated!"     
        
        #Else statement: else if customer doesn't exists store message
        else:
            result['message'] = "Movie not found!"

        #Returning result
        return result

    def delete(self, session, movie_id):
        print("\nDeleting customer details...")
        #Printing the customer_id passed in from customer_dao_test
        print(movie_id)

        #Creating empty dict
        result = {}

        #Getting customer_id from database if exists
        movie = session.query(Movie).get(movie_id)

        #If statement: if customer is found delete customer
        if movie:
            session.delete(movie)          
            session.commit()
      
            result['message'] = "Movie deleted"  

        #Else statement: else if customer is not found store message
        else:  
            result['message'] = "Movie not found"

        #Return result
        return result


    def find_ids(self, session):
        print("\nDisplaying all movie ID...")
        print("\nFinding all movie ids ...")
        
        #Create empty dict
        result = {}

        #Getting all customer infromation from Customer table
        rows = session.query(Movie).all()

        #If statement: if no customer exists store message
        if not rows:
            result['message'] = "No movie found!"
        
        #Else statement: else if customer exists in Customer table print customer(s) IDs
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.movie_id)
                pass               

            result['movie_ids'] = list_ids
        
        #Return result
        return result
