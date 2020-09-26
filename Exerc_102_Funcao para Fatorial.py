def fatorial(n, show=True):
    """
    --> Calcula o fatorial de um número
    :param n: é o número que deve ser calculado
    :param show: é para mostrar ou não como foi feita a fatoração (opcional)
    :return: o numero fatorial de n
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# programa principal
# print (fatorial(5, show=False))
help(fatorial)