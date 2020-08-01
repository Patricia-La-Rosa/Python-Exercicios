tipo = ''
quer = ''
count = 0
count1 = 0
count2 = 0
while True:
    print('-' * 40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)
    id = int(input('Idade: '))
    print('-' * 40)
    tipo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 40)
    while tipo not in 'MF':
        tipo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-' * 40)
    if id >= 18:
        count = count + 1
    if id <= 20 and tipo == 'F':
        count1 = count1 + 1
    if tipo == 'M':
        count2 = count2 + 1
    quer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while quer not in 'SN':
        quer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'N' in quer:
        print(f'Total de pessoas com mais de 18 anos: {count}')
        print(f'Ao todo temos {count2} homens cadastrados')
        print(f'E temos {count1} mulheres com menos de 20 anos')
        break
