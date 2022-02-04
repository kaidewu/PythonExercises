num = input("Dime un número: ")

if(num.isnumeric()):
    par = int(num) % 2
    if(par == 0):
        print("Es un número par")
    else:
        print("Es un número impar")
else:
    print("Por favor, escriba un número entero!")