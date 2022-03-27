try:
    peso = int(input())
    elefantes = list(map(int,input().split()))
    n = 0
    x = list()
    for i in elefantes:
        n += i
        if n <= peso:
            x.append(i)
        elif n > peso:
            break
    print(len(x))
except ValueError:
    print("Error! Escribe numeros")