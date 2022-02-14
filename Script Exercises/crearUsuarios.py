import os

usuarios = os.popen('dsquery user').read().strip()
with open('usuario.csv', 'r') as csvfile:
    for f in csvfile:
        f = f.strip()
        f = f.split(',')
        user = f'"cn={f[0]},cn={f[1]},dc={f[2]},dc={f[3]}"'
        if f[0] not in usuarios:
            os.system(f'dsadd user {user} -disabled no -pwd {f[4]}')
            print(f'Enhorabuena! Has creado el usuario {f[0]}')
        else:
            print(f'El usuario {f[0]} ya existe')