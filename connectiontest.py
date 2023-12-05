#THIS SCRIPT CREATES A CONNECTION TO THE DATABASE

import mysql.connector
from dotenv import load_dotenv
import os

#Collecting environment variables from the .env file
load_dotenv()

#Database credentials
db_host = os.getenv("HOST")
db_port = int(os.getenv("PORT"))
db_user = os.getenv("USER_SQL")
db_password = os.getenv("PASSWORD")
db_database = os.getenv("DATABASE")

#Create connection
connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_database
)

#Check if the connection is successful
if connection.is_connected():
    print("Connected to the database")
    connection.close()
    print("Connection closed")
else:
    print("Failed to connect to the database")
