import math
n = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))
# é uma tupla porque começa com parenteses
print(f'Voce digitou os valores {n}')
print(f'O valor 9 foi digitado {n.count(9)}')
if 3 in n:
    print(f'O valor 3 foi digitado a primeira vez na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram', end = ' ')
for num in n:
    if num % 2 == 0:
        print(num, end = ', ')
