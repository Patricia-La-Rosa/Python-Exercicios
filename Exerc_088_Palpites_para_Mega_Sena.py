from random import randint
lista = list()
cont = 0
tot = 1
jogos = list()
print('-='*20)
print('JOGAR NA MEGASENA')
print('-='*20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= quant:
    cont = 0
    while True:
        computador = randint(0, 60)
        if computador not in lista:
            lista.append(computador)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
print(f'Os números sorteados foram {jogos}')