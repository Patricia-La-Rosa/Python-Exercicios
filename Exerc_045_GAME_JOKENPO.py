from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
comp = randint(0, 2)
# ele vai randomizar o resultado entre 0 e 2
print('-='*20)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jogador]))
# itens substitui computador e jogador
print('-='*20)
if comp == 0: #computador jogou pedra
    if jogador == 0: #jogador jogou pedra
        print('EMPATE')
    elif jogador == 1: #jogador jogou papel
        print('Jogador GANHOU!!!')
    elif jogador == 2: #jogador jogou tesoura
        print('Você PERDEU')
    else:
        print('Jogada inválida')
elif comp == 1: #computador jogou papel
    if jogador == 1: #jogador jogou papel
        print('EMPATE')
    elif jogador == 0: #jogador jogou pedra
        print('Jogador PERDEU')
    elif jogador == 2: #jogador jogou tesoura
        print('Jogador GANHOU!!!')
    else:
        print('Jogada inválida')
elif comp == 2: #computador jogou tesoura
    if jogador == 2: #jogador jogou tesoura
        print('EMPATE')
    elif jogador == 0: #jogador jogou pedra
        print('Jogador GANHOU!!!')
    elif jogador == 1: #jogador jogou papel
        print('Jogador PERDEU')
    else:
        print('Jogada inválida')
