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


def get(document):
    """
    Gets one element from mongodb (tempo collection)
    Filter: Nombre de usuario / Período
    :param document: document to retrieve
    :return:
    """
    user_name = document["Nombre de usuario"]
    period = document["Período"]
    # Establish Filter
    document_filter = {'Nombre de usuario': user_name, 'Período': period}
    return collection_tempo.find_one(document_filter)


def insert(document):
    """
    Inserts an element at mongo db (tempo collection)
    Each element contains the list of tempo registration for user/period
    :param document: element to insert (dictionary)
    :return:
    """
    # Inserts document list into mongo db collection
    collection_tempo.insert_one(document)


def update(document):
    """
    Updates an element at mongo db (tempo collection)
    Each element contains the list of tempo registration for user/period
    Filter: Nombre de usuario / Período
    If document exists we update the registration list
    :param document: element to update
    :return:
    """
    user_name = document["Nombre de usuario"]
    period = document["Período"]
    registration = document["Registros"]
    # Establish Filter
    document_filter = {'Nombre de usuario': user_name, 'Período': period}
    # Set update
    document_update = {'$set': {'Registros': registration}}
    collection_tempo.update_one(document_filter, document_update)


def delete_all():
    """
    Deletes all documents from tempo collection
    :return:
    """
    collection_tempo.delete_many({})
