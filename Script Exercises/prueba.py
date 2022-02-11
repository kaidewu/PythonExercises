import csv
import os
try:
    userfile = input('Dime la ruta del archivo csv: ')
    domainName = input('Dime el nombre de tu dominio (ej. midominio.com): ')
except:
    print('Ha habido un error en la ruta del archivo csv!!')
try:
    domainName = domainName.split('.')
    if len(domainName) == 2:
        if not os.path.exists(userfile):
            print('La ruta del archivo no es correacta!!')
        else:
            with open(userfile, "r") as grupo:
                lista = csv.reader(grupo)
                for cada_linea in lista:
                        user = cada_linea[0]
                        uo = cada_linea[1]
                        password = cada_linea[2]
                        print(f"dsadd user \"cn={user}, cn={uo}, dc={domainName[0]}, dc={domainName[1]}\" -pwd {password} -disabled no")
except:
    print('Ha habido un error')