import sys
import tempo
import log_config as lc


def validate_args(arguments):
    if len(arguments) != 2:
        return False
    else:
        if arguments[1] != '-p' and arguments[1] != '-c' and arguments[1] != '-d' and arguments[1] != '-g' and arguments[1] != '-h':
            return False
    return True


def show_help():
    lc.write_to_log_console(lc.LogLevel.WARNING, '------------------ OPTIONS ------------------')
    lc.write_to_log_console(lc.LogLevel.WARNING, '-h: show help')
    lc.write_to_log_console(lc.LogLevel.WARNING, '-d: download files from directory')
    lc.write_to_log_console(lc.LogLevel.WARNING, '-p: process directory')
    lc.write_to_log_console(lc.LogLevel.WARNING, '-g: get all documents from tempo collection')
    lc.write_to_log_console(lc.LogLevel.WARNING, '-c: clear mongodb tempo collection')
    lc.write_to_log_console(lc.LogLevel.WARNING, '---------------------------------------------')


def tempo_task(arguments):
    try:
        if arguments[1] == '-h':
            show_help()
        if arguments[1] == '-p':
            tempo.process_tempo_directory()
        elif arguments[1] == '-c':
            tempo.clear_tempo_collection()
        elif arguments[1] == '-d':
            tempo.restore_tempo_downloaded()
        elif arguments[1] == '-g':
            tempo.get_tempo_collection()
    except Exception as e:
        lc.write_to_log_console(lc.LogLevel.ERROR, lc.err_general.format(e))


if __name__ == '__main__':
    lc.log_init()
    if validate_args(sys.argv):
        tempo_task(sys.argv)
    else:
        lc.write_to_log_console(lc.LogLevel.WARNING, lc.warn_arguments)
