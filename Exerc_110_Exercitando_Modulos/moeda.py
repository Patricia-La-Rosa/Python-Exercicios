def aumentar (preco = 0,taxaa = 0, formato = False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatacao.
    :param preco: o preco que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco*taxaa/100)
    return res if formato is False else moeda(res)


def diminuir (preco=0,taxar=0, formato = False):
    res = preco - (preco*taxar/100)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)
# esse return com if e o retorno + a função moeda, para formatar o valor


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.',',')
# usado para substituir ponto por virgula IMPORTANTE e acertar casas decimais

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'A metade do preço: \t{metade(preco,True)}')
    print(f'O dobro do preço: \t{dobro(preco, True)}')
    print(f'{aumentar(taxaa)}% de aumento: \t{aumentar(preco,taxaa,True)}')
    print(f'{aumentar(taxar)}% redução: \t\t{diminuir(preco,taxar,True)}')
    print('-' * 40)



