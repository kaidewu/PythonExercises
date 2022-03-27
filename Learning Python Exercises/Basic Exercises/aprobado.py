asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nota = []

for i in asignaturas:
    nota.append(float(input(f"Dime la nota de {i}: ")))

for j in range(len(nota)):
    if nota[j] < 5:
        print(f'Tienes que recuperar {asignaturas[j]}.')