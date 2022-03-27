try:
    num = int(input("Dime un número: "))
    if(num >= 0):
        imprimir = []
        for i in range(num, -1, -1):
            imprimir.append(i)
        for j in range(len(imprimir)):
            if(j == len(imprimir) - 1):
                print(imprimir[j])
            else:
                print(imprimir[j], end=", ")
    else:
        print("No has escrito un número positivo")
except ValueError:
    print("No has escrito un número")