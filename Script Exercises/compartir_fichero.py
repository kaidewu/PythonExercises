#Un fichero csv con un listado de carpetas
#Crear los directorio
#Compartirlos
#grupo usuarios tenga permiso de modificación
import csv
import os
import sys

try:
    with open('directorios.csv', 'r') as carpetas:
        diretorio = csv.reader(carpetas)
        for d in diretorio:
            dirX = ''.join(d)
            lista = dirX.split('\\')
            nomFolder = lista[-1]
            print(dirX)
            if os.path.exists(nomFolder):
                os.system(f'net share {nomFolder}={dirX} /GRANT:Usuarios,CHANGE')
            else:
                os.system(f'mkdir {dirX}')
                os.system(f'net share {nomFolder}={dirX} /GRANT:Usuarios,CHANGE')
except:
    print('ERROR!')
    sys.exit(1)