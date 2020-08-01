print('=' * 40)
print('LOJA BARATÃO')
print('=' * 40)
soma = 0
maior = 0
count = 0
menor = 0
barato = ''
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('R$ '))
    soma = soma + preco
    if preco > 1000:
        maior = maior + 1
        count = count + 1
    if count == 1:
        maior = menor = preco
        barato = prod
    elif preco < menor:
        menor = preco
        barato = prod
    print('='*40)
    seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if seguir == 'N':
        print(f'O total da compra foi R${soma:.2f}')
        print(f'Temos {count} produtos custando mais de R$ 1000')
        print(f'O produto mais barato foi {prod} que custa {preco:.2f}')
        break
