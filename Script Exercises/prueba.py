import os
from xml import dom
try:
    ouName = input('Dime el nombre de la unidad organizativa: ')
    domainName = input('Dime el nombre de tu dominio (ej. midominio.com): ')
except:
    print('Has puesto los parametros mal!!')
domainName = domainName.split('.')
if len(domainName) == 2:
    os.system(f'dsadd ou ou={ouName},dc={domainName[0]},dc={domainName[1]}')
else:
    print('Hay un error al poner el nombre del dominio!!!')