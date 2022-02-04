passwd = "contraseña"

contra = input("Dime la contraseña: ")

if(passwd == contra.lower()):
	print("Las contraseñas coinciden")
else:
	print("Lo siento. La contraseña que has introducido es incorrecta.")