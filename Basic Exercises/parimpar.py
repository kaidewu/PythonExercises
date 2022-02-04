while True:
    try:
        num = int(input("Dime un número mayor de 2: "))
        if(num < 0):
            print("Escriba un número positivo. Por favor!")
        elif(num <= 2):
            print("Escriba un número mayor que 2. Por favor!")
        else:
            if((num % 2) == 0):
                print(f"El {num} es par.")
                break
            else:
                print(f"El {num} es impar.")
                break

    except ValueError:
        print("Escriba un número. Por favor!")