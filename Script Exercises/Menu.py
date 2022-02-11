import os
import socket
import csv

hostnameActual = socket.gethostname()


def main():
    while True:
        print('''
*------------------------------------------------------------------------------*
|                                                                              |
|                                                                              |
|                                                                              |
|                                 Bienvenido                                   |
|                                                                              |
|                                                                              |
|                                                            Hecho por Kaide Wu|
*------------------------------------------------------------------------------*
                 ''')
        try:
            #accion = input('1.- Cambiar tu IP del ordenador\n2.- Cambiar el nombre de la máquina\n3.- Promocionar\n4.- Crear unidades organizativas\n5.- Crear grupos\n6.- Crear usuarios\n7.- Salir\n¿Cuál quieres elegir?: ')
            accion = input('''
1.- Cambiar tu IP del ordenador
2.- Cambiar el nombre de la máquina
3.- Promocionar
4.- Crear unidades organizativas
5.- Crear grupos
6.- Crear usuarios
7.- Salir
¿Cuál quieres elegir?: ''')
        except:
            print('Ha ocurrido un Error!!')
        if accion == '1':
            cambiarIP()
        elif accion == '2':
            cambiarNombre()
        elif accion == '3':
            promocionar()
        elif accion == '4':
            crearUO()
        elif accion == '5':
            crearGrupos()
        elif accion == '6':
            crearUsuarios()
        elif accion == '7':
            print('Adiós!')
            break

def cambiarIP():
    try:
        address = input('Dime la IP que quieres: ')
        submask = input('Dime la mascara que tendra: ')
        gateway = input('Dime la puerta de enlace: ')
        interface = input('Dime que interfaz quieres cambiar:')
    except:
        print('No has puesto bien los parametros!')

    os.system(f'netsh interface ipv4 set address name="{interface}" static {address} {submask} {gateway}')
    print(f'Se ha cambiado correctamente!. Tu nueva IP es {address} con la mascara {submask} y la puerta de enlace {gateway}, en el interfaz {interface}')

def cambiarNombre():
    try:
        name = input('Dime el nuevo nombre para el equipo: ')
    except:
        print('No has puesto bien los parametros!')

    os.system(f'netdom renamecomputer %{hostnameActual}% /Newname "{name}"')

def promocionar():
    try:
        domainDNSName = input('Dime el nombre del dominio DNS: ')
        netbiosName = input('Dime el nombre de la Netbios: ')
    except:
        print('Ha habido un error!!')


    os.system(f'dcpromo /InstallDNS:Yes /ReplicaOrNewDomain:Domain /NewDomain:Forest /NewDomainDNSName:{domainDNSName} /ForestLevel:3 /DomainNetbiosName:{netbiosName} /DomainLevel:3 /ConfirmGc:Yes /CreateDNSDelegation:No /DatabasePath:\"C:\\Windows\\NTDS\" /LogPath:\"C:\\Windows\\NTDS\" /SYSVOLPath:\"C:\\Windows\\SYSVOL\"')
    os.system("shutdown -r -t 0")

def crearUO():
    try:
        ouName = input('Dime la ruta del archivo csv: ')
        domainName = input('Dime el nombre de tu dominio (ej. midominio.com): ')
    except:
        print('Has puesto los parametros mal!!')
    domainName = domainName.split('.')
    if len(domainName) == 2:
        if os.path.exists(ouName):
            with open(ouName, 'r') as csvfile:
                files = csv.reader(csvfile)
                for f in files:
                    os.system(f'dsadd ou ou={f[0]},dc={domainName[0]},dc={domainName[1]}')
        else:
            print('No se ha encontrado el archivo csv!!!')
    else:
        print('Hay un error al poner el nombre del dominio!!!')

def crearGrupos():
    try:
        groupfile = input('Dime la ruta del archivo csv: ')
        domainName = input('Dime el nombre de tu dominio (ej. midominio.com): ')
    except:
        print('Ha habido un error en la ruta del archivo csv!!')
    try:
        domainName = domainName.split('.')
        if len(domainName) == 2:
            if not os.path.exists(groupfile):
                print('La ruta del archivo no es correacta!!')
            else:
                with open(groupfile, "r") as grupo:
                    lista = csv.reader(grupo)
                    for cada_linea in lista:
                            grupo = cada_linea[0]
                            uo = cada_linea[1]
                            os.system(f"dsadd group \"cn={grupo}, cn={uo}, dc={domainName[0]}, dc={domainName[1]}\" -secgrp yes -scope L")
    except:
        print('Ha habido un error')

def crearUsuarios():
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
                            os.system(f"dsadd user \"cn={user}, cn={uo}, dc={domainName[0]}, dc={domainName[1]}\" -pwd {password} -disabled no")
    except:
        print('Ha habido un error')

main()