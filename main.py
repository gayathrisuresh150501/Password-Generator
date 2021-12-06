import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*'

length = int(input('Password length: '))
passReq = int(input('Number of passwords required: '))

for p in range(passReq):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)