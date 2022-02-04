while True:
    try:
        dni = int(input("Dime los números de tu DNI: "))

        letra = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E", ]

        resto = int(dni % 23)
        if (resto >= 0 and resto <= 22):
            print(f"Tu DNI es {dni}{letra[resto]}")
            break
        else:
            print("Error! No has puesto bien los números del DNI bien!")
    except ValueError:
        print("Dime números!")