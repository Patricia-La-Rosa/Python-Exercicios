def ficha(jog = '<desconhecido>', gols = 0):
    print('--'*20)
    print(f'O jogador {jog} fez {gols} gols.')


# programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Total de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)