import boto3
from dotenv import load_dotenv
import os
from conectarse import rds


DB_INSTANCE_ID = os.getenv("DB_INSTANCE_ID")
rds.create_db_instance(
           DBInstanceIdentifier="prueba-codigo", #Nombre de la instancia del RDS
           AllocatedStorage= 20, #El tamaño del RDS
           DBInstanceClass="db.t4g.micro", #Tipo de clase de la base de datos
           Engine="mariadb", # motor de base de datos
           MasterUsername=os.getenv("DB_USER"), #usuario de la base de datos
           MasterUserPassword=os.getenv("DB_PASSWORD"), #password del usuario admin
           PubliclyAccessible=True #Publicar el RDS
 )


waiter = rds.get_waiter('db_instance_available') #Usaremos el waiter para continuar con el código cuando esté disponible el RDS
waiter.wait(DBInstanceIdentifier=DB_INSTANCE_ID)
 

info = rds.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_ID) 
endpoint = info['DBInstances'][0]['Endpoint']['Address'] #IMPORTANTE, necesitamos el endpoint para conectarnos a la base de datos


