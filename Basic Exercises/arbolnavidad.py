try:
    num = int(input("Longitud del árbol de navidad: "))
    x = "*"
    for i in range(1, num + 1):
        print(f"{x * i}")
    if(num <= 0):
        print("Por favor escriba un número positivo!")
except ValueError:
    print("Escriba un número por favor!")