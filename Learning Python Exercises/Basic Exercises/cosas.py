import random as ran

# Calculador de porcentajes
print('Calculador de porcentajes. \nTu me dices cuantas veces tiramos y yo te digo cada cuanto sale cada numero.')
num = int(input('Dime un numero: '))

cero = 0
uno = 0

for i in range(num):
    x = ran.randrange(2)
    if (x == 0):
        cero = cero + 1
    elif (x == 1):
        uno = uno + 1

print(f'El 0 ha salido {(cero * 100) / num}% y el 1 ha salido {(uno * 100) / num}%')