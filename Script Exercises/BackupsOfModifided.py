from datetime import date, datetime
import sys
import os
from zipfile import ZipFile as zip
import shutil

fecha = date.today()
try:
    question = input('Directorio actual ("actual") o Otro directorio ("otro"): ')
    if question == 'actual':
        path = os.getcwd()
    elif question == 'otro':
        path = input('Que directorio quieres: ')
        if not os.path.exists(path):
            print('El directorio no existe')
    else:
        print('Por favor, escriba actual o otro.')
except:
    print('Error!')
    sys.exit(1)

with zip(f'{fecha}.zip', 'w') as compress:
    for directory, subdirectory, files in os.walk(path):
        for f in files:
            os.system(f'attrib -a {os.path.join(directory, f)}')
            compress.write(os.path.join(directory, f), os.path.relpath(os.path.join(directory, f), path))
shutil.move(f'{fecha}.zip', path)
