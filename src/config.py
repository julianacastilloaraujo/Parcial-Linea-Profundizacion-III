#Realizado por Juliana Castillo Araujo
#Parcial 2 
#19 de abril 2024

from pymongo import MongoClient
import certifi

Mongo = MONGO ='mongodb+srv://juliana:ucundinamarca@cluster0.kd118a2.mongodb.net/'
certifi = certifi.where()

def conexion():
    try:
        client = MongoClient(Mongo,tlsCAfile=certifi)
        db =client["bd_productos"]
        print('Conexion Exitosa')
    except ConnectionError:
      print('Error de conexion')
    return db

conexion()