import files
import sys
import tempo
import log_config

# Constantes
ruta_virtual_python = sys.executable
ruta_global_python = sys.base_prefix
ruta_bibliotecas = sys.exec_prefix

path = "C:\\tmp\\file.txt"
file1 = "C:\\tmp\\file.txt"
file2 = "C:\\tmp\\target.txt"
file3 = "C:\\tmp\\excel.txt"
path_excel = "C:\\tmp\\Tempo_SSCCT_Junio_2023\\Usuario_ Natalia Rodríguez Rodríguez_2023-05-26_2023-06-25.xlsx"


def files_test():
    print('Ruta virtual python: ' + ruta_virtual_python)
    print('Ruta global python: ' + ruta_global_python)
    print('Ruta bibliotecas python: ' + ruta_bibliotecas)
    print('LECTURA DE FICHERO')
    print(files.read_text_file(path) + '\r\n')
    print('LECTURA DE FICHERO LÍNEA A LÍNEA')
    print(files.read_text_file_line_by_line(path) + '\r\n')
    print('AÑADIENDO EL CONTENIDO DE UN FICHERO TXT A OTRO...')
    files.append_txt_file_content(file1, file2)
    print('AÑADIENDO TEXTO A UN FICHERO TXT')
    files.append_text_to_file("Añadiendo texto al fichero...", file2)
    print('LECTURA DE FICHERO EXCEL')
    data_frame = files.read_excel_file(path_excel)
    # Muestra la información básica sobre el DataFrame
    print(data_frame.info())
    # Muestra el contenido del Data Frame
    print(data_frame)
    # Delete file
    files.delete_file(file3)
    data_frame.to_csv(file3, sep='\t', index=False)


def tempo_task():
    log_config.log_init()
    try:
        tempo.process_tempo_directory()
    except Exception as e:
        log_config.logging.error(log_config.err_general.format(e))


if __name__ == '__main__':
    # files_test()
    tempo_task()
