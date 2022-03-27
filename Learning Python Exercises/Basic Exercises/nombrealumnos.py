
sexo = input("Dime tu sexo (hombre o mujer): ")

if(sexo.lower() != "hombre" and sexo.lower() != "mujer"):
    print("Por favor escriba si es hombre o mujer!")
else:
    if(sexo.lower() == "hombre"):
        nombre = input("Dime tu nombre (tiene que ser de la N para abajo): ")
        if(nombre.lower() > "n"):
            print("Perteneces al grupo A")
        else:
            print("Perteneces al grupo B.")
    else:
        nombre = input("Dime tu nombre (tiene que ser de la N para abajo): ")
        if(nombre.lower() < "m"):
            print("Perteneces al grupo A")
        else:
            print("Perteneces al grupo B.")