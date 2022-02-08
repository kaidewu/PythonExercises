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
            # Tenemos que convertir el directorio de lista a character
            dirX = ''.join(d)
            # Para poder sacar el nombre de la carpeta que queremos compartir, tenemos que quitar el "\"
            lista = dirX.split('\\')
            nomFolder = lista[-1]
            # Primero miramos si la carpeta existe o no. Si existe que comparta las carpetas
            if os.path.exists(nomFolder):
                os.system(f'net share {nomFolder}={dirX} /GRANT:Usuarios,CHANGE')
            # Si no existe que cree las carpetas y los comparta
            else:
                os.system(f'mkdir {dirX}')
                os.system(f'net share {nomFolder}={dirX} /GRANT:Usuarios,CHANGE')
except:
    print('ERROR!')
    sys.exit(1)