asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for i in asignaturas:
    notas.append(int(input(f"Dime tu nota de {i}: ")))

for j in range(len(asignaturas)):
    print(f"Has sacado un {notas[j]} en {asignaturas[j]}.")