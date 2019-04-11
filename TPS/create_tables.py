import sqlite3

class CreateDB:
    
    def createData(self):
        connection = sqlite3.connect("tps.db")

        with connection:
            connection.execute("CREATE TABLE tps(timestamp DATETIME, temperature NUMERIC, humidity NUMERIC)")
        connection.close()

create = CreateDB()

def main():
    create.createData()

if __name__ == "__main__":
    main()

    