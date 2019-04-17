import sqlite3

class CreateDB:
    
    def createData(self):
        connection = sqlite3.connect("tps.db")

        with connection:
            connection.execute("CREATE TABLE customer(customer_id NUMERIC, firstname TEXT, lastname TEXT, email TEXT, phone_no NUMERIC, dob DATETIME)")
            connection.execute("CREATE TABLE booking(booking_id NUMERIC, customer_id NUMERIC, ticket_id NUMERIC, booking_date DATETIME, num_guest NUMERIC, comment TEXT)")
            connection.execute("CREATE TABLE ticket(ticket_id NUMERIC, cinema_id NUMERIC)")
            connection.execute("CREATE TABLE screening(cinema_id NUMERIC, movie_id NUMERIC, cinema_no NUMERIC, session_time DATETIME, session_date DATETIME)")
            connection.execute("CREATE TABLE movie(movie_id NUMERIC, movie_name TEXT, ratings TEXT)")
        connection.close()

def main():
    create = CreateDB()
    create.createData()

if __name__ == "__main__":
    main()

    