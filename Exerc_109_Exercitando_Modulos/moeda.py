def aumentar (preco = 0,taxa = 0, formato = False):
    res = preco + (preco*taxa/100)
    return res if formato is False else moeda(res)


def diminuir (preco=0,taxa=0, formato = False):
    res = preco - (preco*taxa/100)
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

