import mysql.connector
from dotenv import load_dotenv
import os
import csv

# Load environment variables from the .env file
load_dotenv()

# Database credentials
db_host = os.getenv("HOST")
db_port = int(os.getenv("PORT"))
db_user = os.getenv("USER_SQL")
db_password = os.getenv("PASSWORD")
db_database = os.getenv("DATABASE")

# CSV file path
csv_file_path = "datatest.csv"

# Create connection
connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_database
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to the database")

    # Create a cursor object
    cursor = connection.cursor()

    try:
        # Create the table if it doesn't exist (you can modify this based on your table schema)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS movies (
            id INT PRIMARY KEY,
            name VARCHAR(30),
            year INT
        );
        """
        cursor.execute(create_table_query)
        print("Table created or already exists")

        # Open the CSV file and insert data into the database
        with open(csv_file_path, newline="") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                # Example: Insert data into the database
                insert_query = f"INSERT INTO movies (id, name, year) VALUES ({row['id']}, '{row['name']}', {row['year']});"
                cursor.execute(insert_query)

        # Commit the changes
        connection.commit()
        print("Data inserted successfully")

        cursor.execute("SELECT * FROM movies;")
        result = cursor.fetchall()
        print("Data in movies table:")
        for row in result:
            print(row)

    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed")

else:
    print("Failed to connect to the database")