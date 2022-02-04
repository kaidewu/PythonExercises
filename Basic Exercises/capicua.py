word = input('Dime una palabra: ')
palabra = list(word.lower())
x = 0
num = 0
for i in range(len(palabra) - 1, -1, -1):
    if palabra[i] == palabra[x]:
        num += 1
    x += 1
if num == len(palabra):
    print('Es un palindromo')
else:
    print('No es un palindromo')
