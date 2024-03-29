# Operations with files
import os
import pandas
import shutil

file_not_found_msg = "El fichero no existe: "


def file_exists(path):
    """
    Checks if a file exists
    :param path: file path
    :return: true if file exists, false o
    """
    if os.path.exists(path):
        return True
    else:
        return False


def read_text_file(path):
    """
    Reads a text file.
    If file doesn't exist returns a message
    :param path: file path
    :return: file content
    """
    try:
        with open(path, "r", encoding='utf-8') as file:
            content = file.read()
    except:
        content = file_not_found_msg + path
    return content


def read_text_file_line_by_line(path):
    """
    Reads a text file line by line.
    If file doesn't exist returns a message
    :param path: file path
    :return: file content
    """
    content = ''
    try:
        with open(path, "r", encoding='utf-8') as file:
            for linea in file:
                content = content + linea
    except:
        content = file_not_found_msg + path
    return content


def append_txt_file_content(file1, file2):
    """
    Appends content from one txt file to another
    :param file1: origin file
    :param file2: target file
    """
    content = ""
    if file_exists(file1):
        with open(file1, 'r', encoding='utf-8') as origin_file:
            content = origin_file.read()

    # If target file doesn't exist, it is created ('a')
    with open(file2, 'a', encoding='utf-8') as target_file:
        target_file.write('\r\n' + content)


def append_text_to_file(text, file):
    """
    Appends text to file
    :param text: text to append
    :param file: file to append text to
    """
    # If file doesn't exist, it is created ('a')
    with open(file, 'a', encoding='utf-8') as target_file:
        target_file.write(text + '\r\n')


def read_excel_file(path):
    """
    Reads excel file
    :param path: file path
    :return: file content
    """
    # It uses read_excel method to load data into a DataFrame
    data_frame = pandas.read_excel(path)

    # Filter only cells with content
    return data_frame.dropna(axis=0, how='all').dropna(axis=1, how='all')


def delete_file(file):
    """
    Deletes a file
    :param file: file path
    """
    # Verify if file exists
    if os.path.exists(file):
        # Delete file
        os.remove(file)


def move_file(source_file, target_dir):
    """
    Moves one file to another directory
    :param source_file: file to move (absolute path)
    :param target_dir: target directory (absolute path)
    :return:
    """
    target_file = os.path.join(target_dir, os.path.basename(source_file))
    shutil.move(source_file, target_file)


def copy_files(source_dir, target_dir):
    """
    Copies all files from one directory to another
    :param source_dir: source directory (absolute path)
    :param target_dir: target directory (absolute path)
    :return:
    """
    source_content = os.listdir(source_dir)
    # Get only files, not directories
    source_files = [os.path.join(source_dir, file) for file in source_content if
                    os.path.isfile(os.path.join(source_dir, file))]

    for file in source_files:
        shutil.copy(file, target_dir)
