vocales = ["a", "e", "i", "o", "u"]
palabra = input()
for i in vocales:
    x = 0
    for letras in palabra:
        if letras == i:
            x += 1
    print(f"La vocal {i} aparece {x} veces")