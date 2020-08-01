sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
#upper 0 é para pegar só a primeira letra
while sexo not in 'MF':
    sexo = (input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))