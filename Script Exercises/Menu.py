import os
import sys
import socket

def main():
    while accion != 7:
        print('***************************************************************')
        print('*                          Welcome                            *')
        print('***************************************************************')
        accion = int(input('1 (Cambiar tu IP del ordenador)'))
        if accion == 1:
            cambiarIP()

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
    os.system(f'netdom renamecomputer %{socket.gethostname()}% /Newname "{name}"')

main()