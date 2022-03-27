for i in range(10, 0, -1):
    if (i == 1):
        print(i)
    else:
        print(i, end=", ")


num = []
for i in range(1, 11):
    num.append(i)

num.reverse()
print(num)
