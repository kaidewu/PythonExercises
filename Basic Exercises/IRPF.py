renta = float(input("Dime tu renta anual: "))

if(renta < 10000):
    print(f"Tu tipo impositivo es 5%")
elif (renta < 20000):
    print(f"Tu tipo impositivo es 15%")
elif (renta < 35000):
    print(f"Tu tipo impositivo es 20%")
elif (renta < 60000):
    print(f"Tu tipo impositivo es 30%")
elif (renta > 60000):
    print(f"Tu tipo impositivo es 45%")