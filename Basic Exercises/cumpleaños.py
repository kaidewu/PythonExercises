from ctypes import POINTER


try:
    n = int(input())
    cumple = input().split()
except ValueError:
    print("Error!")
    exit(-1)

dia = list()
mes = list()
año = list()
x = 0
for i in range(n):
    l = cumple[i].split("/")
    dia.append(l[0])
    mes.append(l[1])
    año.append(l[2])
for j in range(1, len(dia)):
    if dia[0] == dia[j] and mes[0] == mes[j]:
        x += 1
if x > 0:
    print("SI")
else:
    print("NO")