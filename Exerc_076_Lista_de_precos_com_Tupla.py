p = ('Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Caneta', 22.30,
    'Livro', 34.90)
print('-'*35)
print(f'{"LISTAGEM DE PREÇOS": ^30}')
#centralizado
print('_'*35)
for poss in range(0,len(p)):
    if poss % 2 == 0:
        print(f'{p[poss]:.<20}', end=' ')
    #     se a posição for par ele imprime, tudo que está na posição 2
    #alinhado a esquerda
    else:
        print(f'R$ {p[poss]:>7.2f}')
print('-'*35)
