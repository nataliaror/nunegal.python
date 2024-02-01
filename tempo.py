# Operations with Tempo files
import json
import files
import os
# To be able to import Python modules that are stored in packages (ex: repository)
import sys
sys.path.append(
    'C:\\Users\\NataliaRodriguez\\OneDrive - Nunegal Consulting SL\\Documentos\\nunegal\\pmo\\cursos\\python\\ficheros')
from repository import mongodb

tempo_directory = 'C:\\tmp\\tempo'

def process_tempo_directory():
    """
    Reads all excel files in tempo directory and insert one registry for each at mongo db
    collection "tempo"
    :return:
    """
    directory_content = os.listdir(tempo_directory)
    files = [os.path.join(tempo_directory, file) for file in directory_content if os.path.isfile(os.path.join(tempo_directory, file))]

    for file in files:
        tempo_dictionary = read_tempo(file)
        tempo_mongodb_dictionary = tempo_mongodb_helper(tempo_dictionary)
        insert_tempo_mongodb(tempo_mongodb_dictionary)

def read_tempo(path_tempo_file):
    """
    Reads excel tempo file and converts it to a list of Dictionaries each with the
    following fields: Nombre completo, Nombre de usuario, Fecha de trabajo, Período
    Clave de Proyecto, Horas, Horas facturadas y Order
    :param path_tempo_file: Full path to the file
    :return: list of dictionaries, each one representing one registry of excel file
    """
    # Read excel to Data Frame
    dataframe_tempo = files.read_excel_file(path_tempo_file)
    # Filter especific columns
    filter_tempo = ['Nombre completo', 'Nombre de usuario', 'Fecha de trabajo', 'Período', 'Clave de Proyecto',
                    'Horas', 'Horas facturadas', 'Order']
    dataframe_filter_tempo = dataframe_tempo[filter_tempo]
    dataframe_filter_tempo_to_json = dataframe_filter_tempo.to_json(orient='records')
    # Convert JSON to dictionary
    return json.loads(dataframe_filter_tempo_to_json)


def tempo_mongodb_helper(tempo_dictionary):
    """
    Formats tempo dictionary to avoid repeated fields
    :param tempo_dictionary: dictionary with excel registries
    :return: dictionary to insert in MongoDB
    """
    tempo_mongodb_registry = {"Nombre completo": tempo_dictionary[0]["Nombre completo"],
                                       "Nombre de usuario": tempo_dictionary[0]["Nombre de usuario"],
                                       "Período": tempo_dictionary[0]["Período"], "Registros": []}

    # Now you can access the values as if they were objects in a list
    for element in tempo_dictionary:
        register_diccionary = {"Order" : element["Order"],
                               "Fecha de trabajo" : element["Fecha de trabajo"],
                               "Clave de Proyecto": element["Clave de Proyecto"],
                               "Horas" : element["Horas"],
                               "Horas facturadas" : element["Horas facturadas"]}
        tempo_mongodb_registry["Registros"].append(register_diccionary)

    return tempo_mongodb_registry


def insert_tempo_mongodb(element):
    """
    Inserts an element at mongo db (tempo collection)
    Each element contains the list of tempo registration for user/period
    :param element: element to insert
    :return:
    """
    mongodb.insert_tempo(element)

