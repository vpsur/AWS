import boto3
from dotenv import load_dotenv
import os

load_dotenv()

session = boto3.session.Session(
   aws_access_key_id=os.getenv("ACCESS_KEY"),
   aws_secret_access_key=os.getenv("SECRET_KEY"),
   aws_session_token=os.getenv("SESSION_TOKEN"),
   region_name=os.getenv("REGION"))


dynamodb = session.client('dynamodb')
print(dynamodb.list_tables())

# tabla = dynamodb.create_table(
#    TableName='ejemplo_tabla_libros',
#    AttributeDefinitions=[
#        {'AttributeName': 'autor', 'AttributeType': 'S'},   # Partition Key
#        {'AttributeName': 'anyo_publicacion', 'AttributeType': 'S'}     # Sort Key
#    ],
#    KeySchema=[
#        {'AttributeName': 'autor', 'KeyType': 'HASH'},  # Partition Key
#        {'AttributeName': 'anyo_publicacion', 'KeyType': 'RANGE'}   # Sort Key
#    ],
#    ProvisionedThroughput={
#        'ReadCapacityUnits': 5, #Numero de lecturas por segundo
#        'WriteCapacityUnits': 5 #Numero de escrituras por segundo
#    }
# )



# tabla = dynamodb.create_table(
#    TableName='ejemplo_tabla_libros_2',
#    AttributeDefinitions=[
#        {'AttributeName': 'autor', 'AttributeType': 'S'},   # Partition Key
#        {'AttributeName': 'anyo_publicacion', 'AttributeType': 'S'}, # Sort Key tabla principal
#        {'AttributeName': 'precio', 'AttributeType': 'N'}  # Sort Key LSI
#    ],
#    KeySchema=[
#        {'AttributeName': 'autor', 'KeyType': 'HASH'}, # Partition Key
#        {'AttributeName': 'anyo_publicacion', 'KeyType': 'RANGE'} # Sort Key tabla principal
#    ],
#    LocalSecondaryIndexes=[
#        {
#            'IndexName': 'PrecioIndex', # Sort Key LSI
#            'KeySchema': [
#                {'AttributeName': 'autor', 'KeyType': 'HASH'},
#                {'AttributeName': 'precio', 'KeyType': 'RANGE'}
#            ],
#            'Projection': {
#                'ProjectionType': 'ALL' # Puede ser ALL, KEYS_ONLY o INCLUDE
#            }
#        }
#    ],
#    ProvisionedThroughput={
#        'ReadCapacityUnits': 5, #Numero de lecturas por segundo
#        'WriteCapacityUnits': 5 #Numero de escrituras por segundo
#    }
# )


dynamodb.update_table(
   TableName='ejemplo_tabla_libros',
   AttributeDefinitions=[
       {'AttributeName': 'genero', 'AttributeType': 'S'},
       {'AttributeName': 'titulo', 'AttributeType': 'S'}
   ],
   GlobalSecondaryIndexUpdates=[
       {
           'Create': {
               'IndexName': 'GeneroTituloIndex',
               'KeySchema': [
                   {'AttributeName': 'genero', 'KeyType': 'HASH'},
                   {'AttributeName': 'titulo', 'KeyType': 'RANGE'}
               ],
               'Projection': {
                   'ProjectionType': 'ALL'
               },
               'ProvisionedThroughput': {
                   'ReadCapacityUnits': 5,
                   'WriteCapacityUnits': 5
               }
           }
       }
   ]
)
