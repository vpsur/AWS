from conectarse import rds
import boto3
from dotenv import load_dotenv
import os
import mysql.connector
from esquema import SQL_MYSQL


DB_INSTANCE_ID = os.getenv("DB_INSTANCE_ID")
info = rds.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_ID) 
endpoint = info['DBInstances'][0]['Endpoint']['Address']

config = {
       "user": os.getenv("DB_USER"),
       "password": os.getenv("DB_PASSWORD"),
       "host": endpoint
      
   }
DB_NAME = os.getenv("DB_NAME")
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(dictionary=True)
cursor.execute(f"USE {DB_NAME}")

cursor.execute("SELECT * FROM libros l")
