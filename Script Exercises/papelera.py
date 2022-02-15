# Importamos todas las libreria que vamos a utilizar
import os
import sys
from datetime import *
import shutil

# Hacemos un control de error en la parte donde te pide la ruta del archivo
try:
    path = input('Dime el archivo que quieres mandar a la papelera: ')
except:
    print('\nHa ocurrido un error!')
    sys.exit(1)

# Le damos una variable a la fecha
fecha = date.today()

# Si el archivo no existe que nos salte un mensaje
if not os.path.exists(path):
    print('No existe el archivo que has puesto!!')
# Si existe que sigua con el script
else:
    # Si la papelera no esta creado la creamos y creamos la carpeta con el nombre de la fecha. Y introducimos los archivos.
    if not os.path.exists('D:\\papelera'):
        os.system('mkdir D:\\papelera')
        os.system(f'mkdir D:\\papelera\\{fecha}')
        shutil.move(path, f'D:\\papelera\\{fecha}')
    # Si ya existe el directorio papelera, miramos si existe la carpeta con el nombre de la fecha para no creado una doble carpeta con la misma fecha
    else:
        if not os.path.exists(f'D:\\papelera\\{fecha}'):
            os.system(f'mkdir D:\\papelera\\{fecha}')
            shutil.move(path, f'D:\\papelera\\{fecha}')
        else:
            shutil.move(path, f'D:\\papelera\\{fecha}')