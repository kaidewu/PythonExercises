import getpass

passwd = "contraseña"

passwdOK = False

while passwdOK == False:
    userpasswd = getpass.getpass("Dime la contraseña: ")
    if(userpasswd == passwd):
        passwdOK = True
    else:
        print("Contraseña Incorrecta!")
print("Contraseña Correcta!")