numeros = []

for i in range(8):
    numeros.append(int(input("Dime los números de la lotería primitiva: ")))

#Ordenar de menor a mayor
numeros.sort()
for j in numeros:
    print(j)