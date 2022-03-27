try:
    alto, ancho = input().split()
    alto = int(alto)
    ancho = int(ancho)
except ValueError:
    print("Error! Dime números.")
    exit(-1)
if alto <= 0 and ancho <= 0 or alto > 1000 and alto > 1000:
    print("Error")
    exit()
suelo = alto * ancho
negras = suelo // 2
blancas = suelo - negras
print(blancas, negras)