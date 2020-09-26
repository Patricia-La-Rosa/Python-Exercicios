import random

def sorteia(lista):
    """
função que sorteia 5 numeros de uma lista de 10
    :param lista:
    :return:
    """
    for count in range(0,5):
        lista.append(random.randint(1,10))
    print(f'Sorteando 5 valores da lista: {lista} PRONTO!')


def somaPar(lista):
    """

    :param lista:
    :return:
    """
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma = soma + n
    print(f'Somando os valores pares da lista: {soma}')

# programa principal
lista = list()
sorteia(lista)
somaPar(lista)

help(sorteia)