from operator import itemgetter
from random import randint
from time import sleep
jogador = {'jogador 1': randint(1,6),
           'jogador 2': randint(1,6),
            'jogador 3': randint(1,6),
            'jogador 4': randint(1,6)}
ranking = dict()
for k, v in jogador.items ():
    print(f'O {k} tirou no dado {v}')
    sleep(1)
print('=-'*20)
print('='*7, 'RANKING DOS JOGADORES', '='*7)
ranking = sorted(jogador.items(), key=itemgetter(1),reverse=True)
sleep(1)
# sorted é para rankear, itemgetter para pegar o item e reverse para reverter a ordenação
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} tirou {v[1]}')
    sleep(1)
