import string

abecedario = list(string.ascii_lowercase)

for i in range(len(abecedario), 1, -1):
    if i % 3 == 0:
        abecedario.pop(i - 1)
print(abecedario)