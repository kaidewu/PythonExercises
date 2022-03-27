from datetime import date
from msilib.schema import Error
from pdb import lasti2lineno
import sys
import os
import shutil
from traceback import print_tb
from urllib.request import ProxyDigestAuthHandler

def treeFolder():
    os.system("dir")
    x = os.popen("dir").read()
    print("ejecución de os.popen().read()")
    print(x)
    
    lineas = os.popen("dir").readlines()
    print("ejecución de os.popen().readlines()")
    print(lineas)
    
    for l in x:
        l = l.strip()
        print(l)

def Copy():
    os.system(f"copy {sys.argv[1]} {sys.argv[2]}")
    Copy()

def CopyControl():
    fichero = sys.argv[1]
    directorio = sys.argv[2]
    if len(sys.argv) == 3:
        if not os.path.isfile(fichero):
            print("No existe el fichero")
        elif not os.path.isfile(directorio):
            os.mkdir(directorio)
            shutil.copy(fichero,directorio)
        else:
            shutil.copy(fichero,directorio)
    else:
        print("No has puesto los valores")

def Buclecopia():
    n = 0       
    if len(sys.argv) >= 3:
            if not os.path.exists(sys.argv[-1]):
                os.mkdir(sys.argv[-1])
                for j in range(1, (len(sys.argv) - 1)):
                    shutil.copy(sys.argv[j],sys.argv[-1])
            else:
                for k in range(1, (len(sys.argv) - 1)):
                    n = n + 1
                    shutil.copy(sys.argv[k],sys.argv[-1])
                if n == 0:
                    print("No se ha copiado ningún fichero")
                elif n == 1:
                    print("1 fichero copiado")
                else:
                    print(f"{n} ficheros copiados")
    else:
        print("No has puestos los valores adecuados")

def dcpromo():
    import socket
    actualhostname = socket.gethostname()
    adaptador = input("Set Interface: ")
    ipaddress = input("Set IP Address: ")
    subnetmask = input("Set subnet Mask: ")
    gateway = input("Set the gateway: ")
    os.system(f"netsh interface ipv4 set address name=\"{adaptador}\" static {ipaddress} {subnetmask} {gateway}")
    hostname = input("Set hostname: ")
    os.system(f"netdom renamecomputer {actualhostname} /newname:{hostname}")
    print(f"IP Address se ha cambiado {ipaddress} {subnetmask}")
    print(f"Se ha cambiado el hostname {actualhostname} por {hostname}")
    domainname = input("Set server Domain Name: ")
    os.system(f"Install-ADDSForest -DomainName {domainname} -InstallDNS")
    os.system("shutdown -r -t 0")
    dcpromo()

#def dir2():
#    import locale
#    locale.setlocale(locale.LC_ALL, "")
#    ruta = os.path.abspath(input("Escribe la ruta: "))
#    tamaño = int(sys.argv[1])
#    for folder, subfolders, files in os.walk(ruta):
#        for file in files:
#            size = os.stat(os.path.join(folder, file)).st_size
#            if int(size) >= tamaño:
#                archivos = os.path.join(folder, file)
#                os.system(f"dir /Aa /b {archivos}")
#    dir2()

def dir2():
    import locale
    locale.setlocale(locale.LC_ALL, "")
    tamaño = int(sys.argv[1])
    filesimple = os.popen(f"dir /a-d /o-S").readlines()
    for i in range(5, len(filesimple) - 1):
        l = filesimple[i].strip()
        l = l.split()
        n = locale.atoi(l[2])
        if n >= tamaño:
            print(filesimple[i].strip())
    dir2()

def dsquery():
    comando = os.popen("dsquery user").read().split()
    for i in comando:
        n = i.split(",")
        user = n[0].split("=")
        if len(user) > 1:
            print(user[1])
    dsquery()

def copy5():
    origen = sys.argv[1]
    destino = sys.argv[-1]
    if len(sys.argv) == 3:
        if not os.path.exists(destino):
            os.system(f"mkdir {destino}")
            os.system(f"xcopy {origen} {destino}")
        else:
            os.system(f"xcopy {origen} {destino}")
    elif len(sys.argv) == 2:
        if not os.path.exists(destino):
            os.system(f"mkdir {destino}")
            os.system(f"xcopy . {destino}")
        else:
            os.system(f"xcopy . {destino}")
    else:
        print("Error!")
    copy5()

def multiping():
    red = sys.argv[-1]
    string = "Host de destino inaccesible"
    for i in range(1, 255):
        ping = os.popen(f"ping {red}.{i}").readlines()
        if string in str(ping):
            print(f"La IP {red}.{i} no es accesible")
        else:
            print(f"La IP {red}.{i} es accesible")
    multiping()
    
def ficherotest():
    with open("asereje.txt", "w") as cancion:
        with open("pepe.txt", "r") as test:
            for l in test:
                cancion.write(l)
    os.system("asereje.txt")
    ficherotest()

def escribirficheros():
    comprovacion = input("¿Quieres escribir algo en el fichero?\n")
    if comprovacion == "No" or comprovacion  == "no" or comprovacion == "NO" or comprovacion == "":
        compro = False
        print("Adiós")
    else:
        compro = True
    with open("escrituratest.txt", "w") as fichero:
        while compro == True:
            texto = input("Escribe la frase: ")
            fichero.write(texto, "\n")
            x = input("¿Quieres seguir escribiendo?\n")
            if x == "No" or x  == "no" or x == "NO" or x == "":
                print("Adiós")
                break
    escribirficheros()
    
def tablanum():
    num = int(input("Escribe un número del 1 al 10: "))
    if num > 0 and num < 11:
        with open(f"tabla-{num}.txt", "w") as tabla:
            for i in range(1, 11):
                tabla.write(f"{num}x{i}={num*i}\n")
        os.system(f"tabla-{num}.txt")
    else:
        print("Escribe un número del 1 al 10, porfavor!")
    tablanum()

def leerfichero():
    try:
        num = int(input("Escribe un número del 1 al 10: "))
    except:
        print("Ha ocurrido un problema!")
        sys.exit(-1)
    else:
        if not os.path.exists(f"tabla-{num}.txt"):
            print("No existe el fichero!")
        else:
            with open(f"tabla-{num}.txt", "r") as tabla:
                print(tabla.read())
    leerfichero()

def leerlineasfichero():
    try:
        num = int(input("Escribe un número del 1 al 10: "))
        numlinea = int(input("Escribe que lineas quieres leer: "))
    except:
        print("Ha ocurrido un problema!")
        sys.exit(-1)
    else:
        if not os.path.exists(f"tabla-{num}.txt"):
            print("No existe el fichero!")
        else:
            with open(f"tabla-{num}.txt", "r") as tabla:
                x = 0
                for i in tabla:
                    x += 1
                    if x == numlinea:
                        print(i)
    leerlineasfichero()

def covidvalencia():
    import csv
    try:
        with open('casos_tecnica_ccaa.csv', 'r') as casos:
            with open('casosvc.txt', 'w') as casosvc:
                lista = csv.reader(casos)
                for cada_linea in lista:
                    if cada_linea[0] == 'VC':
                        casosvc.write(', '.join(cada_linea) + '\n')             
    except:
        print("Ha ocurrido un error!")
        sys.exit(-1)        
    covidvalencia()

def totalcovid():
    import csv
    numcasos = 0
    try:
        with open('casos_tecnica_ccaa.csv', 'r') as casos:
            with open('casosvc-totales.txt', 'w') as casosvc:
                lista = csv.reader(casos)
                for cada_linea in lista:
                    if cada_linea[0] == 'VC':
                        numcasos += int(cada_linea[2])
                        casosvc.write(', '.join(cada_linea) + ', ' + str(numcasos) + '\n')
    except:
        print("Ha ocurrido un error!")
        sys.exit(-1)   
    totalcovid()
    
def comprobacioncovid():
    import csv
    numcasos = 0
    try:
        with open('casos_tecnica_ccaa.csv', 'r') as casos:
            with open('casosvc-comprobacion.txt', 'w') as casosvc:
                lista = csv.reader(casos)
                for cada_linea in lista:
                    if cada_linea[0] == 'VC':
                        x = ""
                        numcasos += int(cada_linea[2])
                        for i in range(2, 8):
                            if cada_linea[i] == 0 or not cada_linea[i].isdecimal():
                                cada_linea[i] = "0"
                                x += cada_linea[i] 
                        casosvc.write(cada_linea[0] + ", "+ cada_linea[1] + ", " + ", ".join(x) + ", " + numcasos + "\n")
    except:
        print(Error)
        sys.exit(-1)   
    comprobacioncovid()
    
def crearusuarios():
    import csv
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
    crearusuarios()

def creargrupos():
    import csv
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
    creargrupos()
    
def añadirusuagru():  
    import csv
    contador = 0
    try:
        with open("usuaygrupo.csv", "r") as grupo:
            lista = csv.reader(grupo)
            for cada_linea in lista:
                if contador == 1:
                    usuario = cada_linea[0]
                    uoUser = cada_linea[1]
                    group = cada_linea[2]
                    uoGroup = cada_linea[3]
                    os.system(f"dsmod group \"cn={group}, cn={uoGroup}, dc=dominio14, dc=local\" -addmbr \"cn={usuario}, cn={uoUser}, dc=dominio14, dc=local\"")
                contador = 1
    except:
        print("Ha habido un Error!")
        sys.exit(-1)            
    añadirusuagru()

def copiaseguridad():
    from zipfile import ZipFile
    files = os.listdir(".")
    with ZipFile('backupsDesktopFiles.zip', 'w') as zipfile:
        for each_file in files:
            # Opcional Si lo que queremos es solo hacer un bakcup de ficheros y nos directorio y ficheros
            if os.path.isfile(each_file):
                zipfile.write(each_file)
    copiaseguridad()

def copiaseguridadModificado():
    from zipfile import ZipFile
    files = os.popen("dir /AA /B").readlines()
    with ZipFile('backupsDesktopFiles.zip', 'w') as zipfile:
        for each_file in files:
            each_file = each_file.strip()
            zipfile.write(each_file)
    copiaseguridadModificado()

def backupModificadoQuitandoelA():
    from zipfile import ZipFile
    files = os.popen("dir /AA /B").readlines()
    with ZipFile('backupsDesktopFiles.zip', 'w') as zipfile:
        for each_file in files:
            each_file = each_file.strip()
            zipfile.write(each_file)
            os.system(f"attrib -a {each_file}")
    backupModificadoQuitandoelA()

def backupconfecha():
    from zipfile import ZipFile
    import datetime as dt
    fecha = dt.date.today()
    files = os.popen("dir /AA /B").readlines()
    with ZipFile(f'{fecha}.zip', 'w') as zipfile:
        for each_file in files:
            each_file = each_file.strip()
            zipfile.write(each_file)
            os.system(f"attrib -a {each_file}")
    backupconfecha()

def infopc():
    import psutil
    perc_cpu = psutil.cpu_percent(interval=1, percpu=True)
    mem_virt = int(psutil.virtual_memory().used / (1024 ** 2))
    avail_mem = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    print(f'''Estado actual del PC: La CPU esta al {perc_cpu}% Usando {mem_virt} Mb de memoria Quedando {avail_mem}% memoria libre''')
    infopc()
    
def backupFull():
    from zipfile import ZipFile
    import datetime as dt
    fecha = dt.date.today()
    files = os.popen("dir /AA /S /B").readlines()
    with ZipFile(f'{fecha}.zip', 'w') as zipfile:
        for each_file in files:
            each_file = each_file.strip()
            zipfile.write(each_file)
            os.system(f"attrib -a {each_file}")
    backupFull()
    
def backup1000():
    from zipfile import ZipFile as zip
    import datetime as dt
    limitsize = sys.argv[1]
    fecha = dt.date.today()
    files = os.popen('dir /AA /S /B').readlines()
    #files = os.popen('dir /S /B').readlines()
    with zip(f'{fecha}.zip', 'w') as comprimido:
        for f in files:
            f = f.strip()
            if not f.endswith('.zip'):
                if os.stat(f).st_size >= int(limitsize):
                    comprimido.write(f)
            os.system(f"attrib -a {f}")
    backup1000()

