try:
    cantidad = float(input("Dime una cantidad: "))
    interes = float(input("Dime el TAE: "))
    años = int(input("Dime cuantos años quieres invertir: "))

    for i in range(1, años + 1):
        cantidad += cantidad * interes / 100
        print(f"En el {i} años obtienes es {round(cantidad, 2)}€")
        años-= 1
except ValueError:
    print("No has puesto números")