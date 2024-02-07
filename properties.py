import configparser

config = configparser.ConfigParser()
config.read('properties.ini')

########## MONGODB PROPERTIES ############################
uri = config['mongodb.properties']['uri']
database = config['mongodb.properties']['database']
collection = config['mongodb.properties']['collection']
##########################################################

############## LOG PROPERTIES ############################
log_directory = config['log.properties']['log_dir']
##########################################################

############## TEMPO PROPERTIES ##########################
tempo_directory = config['tempo.properties']['tempo_dir']
downloaded_directory = config['tempo.properties']['downloaded_dir']
processed_directory = config['tempo.properties']['processed_dir']
error_directory = config['tempo.properties']['error_dir']
##########################################################
