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


# dynamodb.update_table(
#    TableName='ejemplo_tabla_libros',
#    AttributeDefinitions=[
#        {'AttributeName': 'genero', 'AttributeType': 'S'},
#        {'AttributeName': 'titulo', 'AttributeType': 'S'}
#    ],
#    GlobalSecondaryIndexUpdates=[
#        {
#            'Create': {
#                'IndexName': 'GeneroTituloIndex',
#                'KeySchema': [
#                    {'AttributeName': 'genero', 'KeyType': 'HASH'},
#                    {'AttributeName': 'titulo', 'KeyType': 'RANGE'}
#                ],
#                'Projection': {
#                    'ProjectionType': 'ALL'
#                },
#                'ProvisionedThroughput': {
#                    'ReadCapacityUnits': 5,
#                    'WriteCapacityUnits': 5
#                }
#            }
#        }
#    ]
# )


# dynamodb = session.resource('dynamodb')

# tabla = dynamodb.Table(os.getenv("TABLA"))
# libros = [
#    {'autor': 'García Márquez', 'anyo_publicacion': '1967', 'titulo': 'Cien años de soledad'},
#    {'autor': 'Isabel Allende', 'anyo_publicacion': '1982', 'titulo': 'La casa de los espíritus'},
#    {'autor': 'J.K. Rowling', 'anyo_publicacion': '1997', 'titulo': 'Harry Potter y la piedra filosofal'},
#    {'autor': 'George Orwell', 'anyo_publicacion': '1949', 'titulo': '1984'},
#    {'autor': 'Jane Austen', 'anyo_publicacion': '1813', 'titulo': 'Orgullo y prejuicio'}
# ]

# for libro in libros:
#    tabla.put_item(
#        Item={
#            'autor': libro['autor'],
#            'anyo_publicacion': libro['anyo_publicacion'],
#            'titulo': libro['titulo'],
#        }
#    )
