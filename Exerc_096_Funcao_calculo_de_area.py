def area(larg, compr):
    return (larg*compr)


print('Controle de Terrenos')
print('-'*30)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {larg} x {compr} é de {area(larg,compr)}m.')
