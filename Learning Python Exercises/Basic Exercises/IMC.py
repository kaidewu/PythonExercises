# IMC

peso = float(input('Dime tu peso (Kg): '))
altura = float(input('Dime tu altura (m): '))

imc = peso / (altura ** 2)

print(f'Tu indice de masa corporal es {round(imc, 2)}')