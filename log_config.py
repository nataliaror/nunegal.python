import logging
import properties
from enum import Enum


class LogLevel(Enum):
    INFO = 1
    DEBUG = 2
    WARNING = 3
    ERROR = 4


# Log file location
log_file = properties.log_directory

# Log messages (info, warnings, errors)
warn_arguments = 'You must enter argument: "-h" help, "-p" process, "-c" clear, "-d" download, "-g" get all'
warn_no_files_to_process = 'There are no new files to process.'
warn_tempo_empty_collection = 'There are no tempo documents. The collection is empty.'
info_file_processed = 'File succesfully processed: {0}'
info_clear_tempo_collection = 'Collection: tempo - Cleared!'
info_files_moved_from_downloaded = 'Files have been moved to processing tempo directory.'
err_processing_file = 'Error processing file: {0} - Exception: {1}'
err_general = 'An error occurred - Exception: {0}'

# Log configurations
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def write_to_log_console(level, message):
    print(str(level) + ' - ' + message)
    if level == LogLevel.INFO:
        logging.info(message)
    if level == LogLevel.DEBUG:
        logging.debug(message)
    if level == LogLevel.WARNING:
        logging.warning(message)
    if level == LogLevel.ERROR:
        logging.error(message)


def log_init():
    write_to_log_console(LogLevel.INFO, "=================================================================")
    write_to_log_console(LogLevel.INFO,'======================= PROCESS EXECUTION =======================')
    write_to_log_console(LogLevel.INFO, "=================================================================")
