# Operations with Tempo files
import json
import files
import os
# To be able to import Python modules that are stored in packages (ex: repository)
import sys
import log_config

sys.path.append(
    'C:\\Users\\NataliaRodriguez\\OneDrive - Nunegal Consulting SL\\Documentos\\nunegal\\pmo\\cursos\\python\\ficheros')
from repository import mongodb

tempo_directory = 'C:\\tmp\\tempo'
tempo_processed_dir = 'C:\\tmp\\tempo\\processed'
tempo_error_dir = 'C:\\tmp\\tempo\\error'


def process_tempo_directory():
    """
    Reads all excel files in tempo directory and inserts/updates one registry for each at mongo db
    collection "tempo"
    :return:
    """
    directory_content = os.listdir(tempo_directory)
    # Get only files, not directories
    directory_files = [os.path.join(tempo_directory, file) for file in directory_content if
                       os.path.isfile(os.path.join(tempo_directory, file))]

    for file in directory_files:
        try:
            tempo_dictionary = read_tempo(file)
            document = tempo_document(tempo_dictionary)
            if mongodb.get(document) is None:
                mongodb.insert(document)
            else:
                mongodb.update(document)
            files.move_file(file, tempo_processed_dir)
            log_config.logging.info(log_config.info_file_processed.format(file))
        except Exception as e:
            log_config.logging.error(log_config.err_processing_file.format(file, e))
            files.move_file(file, tempo_error_dir)


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


def tempo_document(tempo_dictionary):
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
        register_diccionary = {"Order": element["Order"],
                               "Fecha de trabajo": element["Fecha de trabajo"],
                               "Clave de Proyecto": element["Clave de Proyecto"],
                               "Horas": element["Horas"],
                               "Horas facturadas": element["Horas facturadas"]}
        tempo_mongodb_registry["Registros"].append(register_diccionary)

    return tempo_mongodb_registry
