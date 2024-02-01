# Mongo DB Atlas Repository
import json
import certifi
from pymongo import MongoClient

# For connecting to MongoDB Server with SSL Handshake
ca = certifi.where()
# Connection String
connection_string = 'mongodb+srv://admin:admin@my-storage.oa0cskx.mongodb.net/?retryWrites=true&w=majority'
# Client creation
mongodb_client = MongoClient(connection_string, tlsCAFile=ca)
# Select database
database = mongodb_client['nunegal']
# Select collection
collection_tempo = database['tempo']



def insert_tempo(element):
    """
    Inserts an element at mongo db (tempo collection)
    Each element contains the list of tempo registration for user/period
    :param element: element to insert
    :return:
    """
    # Inserts document list into mongo db collection
    collection_tempo.insert_one(element)

