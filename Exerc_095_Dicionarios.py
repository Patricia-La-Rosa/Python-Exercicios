jogador = dict()
partida = list()
time = list()
cont = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    partida.clear()
    for x in range (1,(tot+1)):
        partida.append(int(input(f'Quantos gols na partida {x}: ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        seg = str(input('Quer continuar? [S/N] ')).upper()[0]
        if seg in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if seg == 'N':
        break
print('=-'*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-'*60)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
        print('ENCERRANDO...')
    if busca >= (len(time)):
        print(f'ERRO, não existe jogador com código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, v in enumerate(partida):
            print(f'    => Na partida {i + 1}, fez {v} gols.')
    break

