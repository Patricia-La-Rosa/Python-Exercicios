def notas(*n,sit = '<desconhecida>'):
    """
    DICIONÁRIO COM NOTAS E SITUACAO de vários alunos
    :param n: VÁRIAS NOTAS
    :param sit: SITUAÇÃO, somente se for colocada
    :return: DICIONÁRIO COMPLETO
    """
    r = dict()
    r['total']= len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/r['total']
    if sit == True:
        if r['media'] <= 6:
            r['Situação'] = 'RUIM'
        if 6 <= r['media'] <=8:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'ÓTIMA'
    return r

# programa principal
resp = notas(8.5, 8.5, 7.5, sit=True)
print(resp)
# help(notas)