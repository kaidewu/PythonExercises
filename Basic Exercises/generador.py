from random import choice
import string

length = int(input('Length of your password: '))

symbol = '!@#$%^&*()_+-][}{;:.,></?\|'
chars = string.ascii_letters + string.digits + symbol

passwd = "".join(choice(chars) for i in range(length))

print(f'Your password is: {passwd}')