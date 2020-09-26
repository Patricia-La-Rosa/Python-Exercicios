def voto(ano):
    from datetime import date
    atual = date.today().year
    print('--' * 20)
    idade = atual-ano
    if idade < 16:
        return f'Com {idade} anos o VOTO É NEGADO.'
    elif 16<= idade < 18 or idade > 65:
        return f'Com {idade} anos o VOTO É OPCIONAL'
    else:
        return f'Com {idade} anos o VOTO É OBRIGATÓRIO'


print(voto(1974))
