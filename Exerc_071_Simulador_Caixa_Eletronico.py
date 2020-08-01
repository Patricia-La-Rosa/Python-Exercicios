from math import trunc
print('='*40)
print('{:^30}'.format('BANCO CEV'))
# modo de colocar o banco cev no meio
print('='*40)
div50 = 0
div10 = 0
div1 = 0
while True:
    n = int(input('Qual valor você quer sacar? R$ '))
    if n % 50 == 0:
        div50 = n / 50
        resto50 = n % 50
        print(f'Total de {div50} cédulas de R$50')
        break
    if n % 50 != 0:
        div50 = n / 50
        resto50 = n % 50
        div10 = resto50/10
        resto10 = n % 10
        print(f'Total de {div50} cédulas de R$50')
        print(f'Total de {div10} cédulas de R$ 10')
        if n % 10 == 0:
            break
        if n % 10 !=0:
            div1 = resto10 / 1
            resto1 = n % 1
            print(f'total de {div1} cédulas de R$ 1')
            break
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia')