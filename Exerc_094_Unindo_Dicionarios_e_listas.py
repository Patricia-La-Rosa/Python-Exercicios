galera = list()
pessoa = dict()
soma = media = 0
count = 0
count1 = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    count = count + 1
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while pessoa['sexo'] not in 'MmFf':
        print('Por favor, digite apenas M ou F')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    seg = str(input('Quer continuar? [S/N] '))
    if seg in 'Nn':
        break
    while seg not in 'SsNn':
        print('ERRO! Responda apenas S ou N')
        seg = str(input('Quer continuar? [S/N] '))
print('=-'*50)
print(f'A) Temos um total de {count} pessoas cadastradas.')
media = soma/count
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D) A lista de pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()

