edad = int(input("Dime tu edad: "))
if(edad < 16):
    print("Puto niño")
    exit
else:
    ingresos = float(input("Dime tus ingresos mensuales: "))
    if(ingresos > 1000):
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")
