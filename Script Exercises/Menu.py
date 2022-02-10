import os
import sys
import socket
import csv

hostnameActual = socket.gethostname()

def main():
    while True:
        print('***************************************************************')
        print('*                          Welcome                            *')
        print('***************************************************************')
        accion = input('1.- Cambiar tu IP del ordenador\n2.- Cambiar el nombre de la máquina\n3.- Promocionar\n4.- Crear unidades organizativas\n5.- Crear grupos\n6.- Crear usuarios\n7.- Salir\n¿Cuál quieres elegir?: ')
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
        sys.exit(1)
    os.system(f'netsh interface ipv4 set address name="{interface}" static {address} {submask} {gateway}')
    print(f'Se ha cambiado correctamente!. Tu nueva IP es {address} con la mascara {submask} y la puerta de enlace {gateway}, en el interfaz {interface}')

def cambiarNombre():
    try:
        name = input('Dime el nuevo nombre para el equipo: ')
    except:
        print('No has puesto bien los parametros!')
        sys.exit(1)
    os.system(f'netdom renamecomputer %{hostnameActual}% /Newname "{name}"')

def promocionar():
    try:
        domainDNSName = input('Dime el nombre del dominio DNS: ')
        netbiosName = input('Dime el nombre de la Netbios: ')
    except:
        print('Ha habido un error!!')
        sys.exit(1)

    os.system(f'dcpromo /InstallDNS:Yes /ReplicaOrNewDomain:Domain /NewDomain:Forest /NewDomainDNSName:{domainDNSName} /ForestLevel:3 /DomainNetbiosName:{netbiosName} /DomainLevel:3 /ConfirmGc:Yes /CreateDNSDelegation:No /DatabasePath:\"C:\\Windows\\NTDS\" /LogPath:\"C:\\Windows\\NTDS\" /SYSVOLPath:\"C:\\Windows\\SYSVOL\"')
    os.system("shutdown -r -t 0")

def crearUO():
    print

def crearGrupos():
    contador = 0
    try:
        with open("grupos.csv", "r") as grupo:
            lista = csv.reader(grupo)
            for cada_linea in lista:
                if contador == 1:
                    grupo = cada_linea[0]
                    uo = cada_linea[1]
                    os.system(f"dsadd group \"cn={grupo}, cn={uo}, dc=dominio14, dc=local\" -secgrp yes -scope L")
                contador = 1
    except:
        print("Ha habido un Error!")
        sys.exit(-1)

def crearUsuarios():
    contador = 0
    try:
        with open("usuarios.csv", "r") as usuarios:
            lista = csv.reader(usuarios)
            for cada_linea in lista:
                if contador == 1:
                    usuario = cada_linea[0]
                    uo = cada_linea[1]
                    passwd = cada_linea[2]
                    os.system(f"dsadd user \"cn={usuario}, cn={uo}, dc=dominio14, dc=local\" -pwd {passwd} -disabled no")
                contador = 1
    except:
        print("Ha habido un Error!")
        sys.exit(-1)

main()