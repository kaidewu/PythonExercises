#Un fichero csv con un listado de carpetas
#Crear los directorio
#Compartirlos
#grupo usuarios tenga permiso de modificación
import csv
from dataclasses import replace
import os
from re import I
import shutil
import sys

#try:
with open('directorios.csv', 'r') as carpetas:
    diretorio = csv.reader(carpetas)
    for d in diretorio:
        dirX = ''.join(d)
        lista = dirX.split('\\')
        nomFolder = lista[-1]
        if os.path.exists(nomFolder):
            os.system(f'net share {nomFolder}=K:\{d} /GRANT:everyone,CHANGE')
        else:
            os.system(f'mkdir {d}')
            os.system(f'net share {nomFolder}=K:\{d} /GRANT:everyone,CHANGE')
#except:
#    print('ERROR!')
#    sys.exit(1)
