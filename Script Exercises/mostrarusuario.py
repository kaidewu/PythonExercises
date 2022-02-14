# Muestra todos los usuarios que existe en el windows server

import os

contenido = os.popen('dsquery user').readlines()
usuarios = list()
for i in range(len(contenido)):
    linea = contenido[i].strip()
    linea = linea.split(',')
    linea = linea[0].split('CN=')
    usuarios.append(linea[1])
usuario = ', '.join(usuarios)
print(f'Los usuarios son {usuario}')
