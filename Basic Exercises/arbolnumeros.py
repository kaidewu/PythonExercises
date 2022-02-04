try:
    num = int(input("Dime un número: "))
    if((num % 2) != 0):
        for i in range(1, num + 1, 2):
            for j in range(i, 0, -2):
                print(j, end=" ")
            print("")
    else:
        print("Dime números impar.")
except ValueError:
    print("Por favor introduzca un número!")