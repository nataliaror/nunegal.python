import logging

# Log file and error messages
log_file = 'C:\\tmp\\tempo_log.txt'
info_file_processed = 'File succesfully processed: {0}'
err_processing_file = 'Error processing file: {0} - Exception: {1}'
err_general = 'An error occurred - Exception: {0}'

# Log configurations
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_init():
    logging.info('=================================================================')
    logging.info('======================= PROCESS EXECUTION =======================')
    logging.info('=================================================================')
