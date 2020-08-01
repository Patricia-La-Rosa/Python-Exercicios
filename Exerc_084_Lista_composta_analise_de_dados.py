temp = []
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('NOME: ')))
    temp.append(float(input('PESO: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp [1] > maior:
            maior = temp[1]
        if temp [1] < menor:
            menor = temp[1]
    #     se o contador igual a zero significa que não tenho nada cadastrador, então

    princ.append(temp[:])
    # a lista princ recebe temp
    temp.clear()
    # para limpar o temp e não repetir os dados
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if "N" in resp:
        break
print('=-'*30)
print(f'O número de pessoas cadastradas foi de {len(princ)}')
# vc pode criar um contador ou usar o len
print(f'Os dados foram {princ}')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}',end='')
print()
print(f'o menor peso foi de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}',end='')
print()
