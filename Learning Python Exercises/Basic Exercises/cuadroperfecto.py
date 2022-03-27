import math
try:
    num = int(input())
except ValueError:
    print("Error! Dime un número")
    exit(-1)

x = 1
n = int(math.sqrt(num))
while x >= 1 and x <= 2 ** 31:
    if n * n == num:
        print(x)
        break
    else:
        y = num * x
        k = int(math.sqrt(y))
        if k * k == y:
            print(x)
            break
    x += 1