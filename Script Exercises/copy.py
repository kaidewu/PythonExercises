import sys
import os
import shutil

# A los argumentos meterlo en variables
destination_folder = sys.argv[-1]
source_copy = sys.argv[1]

# Controlador de error de los argumentos
if not os.path.exists(source_copy):
    print('No existe el archivo o directorio!!!')
    print('Nota: Si el archivo esta en el mismo directorio, con solo poner el nombre del archivo o carpeta sirve pero si no esta en el mismo directorio es necesario poner la ruta absoluta del archivo o directorio. Igual que el destino donde quieres copiarlo, si pones solo el nombre se te creara donde estas ahora pero si quieres un lugar especifico tienes que ponerlo con la ruta especifica.')

# Tiene que haber 3 argumentos (la archivo.py, la carpeta o archivo y a que directorio quieres copiarlo)
if len(sys.argv) == 3:
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
        shutil.copy(source_copy, destination_folder)
    else:
        shutil.copy(source_copy, destination_folder)
else:
    print("No has puestos los valores adecuados")