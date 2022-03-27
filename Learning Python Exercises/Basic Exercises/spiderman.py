try:
    print("Input")
    pruebas = int(input())
    salida = list()
    for i in range(pruebas):
        posicion = list( map(int,input().split()))
        BombaA = abs(posicion[0] - posicion[1])
        BombaB = abs(posicion[0] - posicion[2])
        AB = abs(posicion[1] - posicion[2])
        if (posicion[0] >= 0 and posicion[0] <= 10000) and (posicion[1] >= 0 and posicion[1] <= 10000) and (posicion[2] >= 0 and posicion[2] <= 10000):
            salida.append(BombaA + AB)
        else:
            print("posiciones del 0 a 10000")
    print("Output")
    for j in salida:
        print(j)
except ValueError:
    print("Escribe numeros!")