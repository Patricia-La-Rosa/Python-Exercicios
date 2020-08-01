from random import randint
from time import sleep
computador = randint (0,5) #Este comando faz o computador PENSAR
print('-='*30)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print ('-='*30)
jogador = int(input('Em que número eu pensei?  '))
print('Processando ...')
sleep(3) #sleep serve para o computador esperar para ler o restante do código
if computador == jogador:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('Você errou!!! Eu pensei no número {} e você pensou no {}. Tente novamente'.format(computador,jogador))
