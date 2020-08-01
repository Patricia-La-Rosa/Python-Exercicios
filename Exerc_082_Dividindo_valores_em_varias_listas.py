num = list ()
pares = list ()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if 'N' in resp:
        break
for i, v in enumerate(num):
    #utilizo esta forma para que ele verifique e cada item de enumerate
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)
print('=-'*30)
print(f'A lista completa é {num}')
print(f'Os números impares são {impares}')
print(f'Os números pares são {pares}')