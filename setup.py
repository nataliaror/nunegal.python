# Script to build standalone executable from Python
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# Include 'dns' package because 'cx_freeze' doesn't pick dns mongodb dependency
packages = ['dns']
include_files = ['properties.ini']  # Another files to include in the build (properties, etc)
build_options = {'packages': packages, 'excludes': [], 'include_files': include_files}

##### SELECT EXECUTABLE TYPE #######
import sys
# Graphic User Interface Application
#base = 'Win32GUI' if sys.platform == 'win32' else None

# Windows Service
#base = 'Win32Service' if sys.platform=='win32' else None

# Console Application
base = 'console'
#####################################

executables = [
    Executable('main.py', base=base)
]

setup(name='tempo_task',
      version='1.0',
      description='Perform Tempo tasks',
      options={'build_exe': build_options},
      executables=executables)
