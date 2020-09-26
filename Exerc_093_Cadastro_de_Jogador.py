jogador = dict()
partida = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for x in range (1,(tot + 1)):
    partida.append(int(input(f'Quantos gols na partida {x}: ')))
    #não pode esquecer de dar append em uma lista
jogador['gols'] = partida
jogador['total'] = sum(partida)
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas')
for i, v in enumerate(partida):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
