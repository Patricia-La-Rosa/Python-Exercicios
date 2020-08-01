soma = 0
media = 0
count = 0
maioridadehomem = 0
nomevelho = ''
#este é um modo de inicializar minhas variáveis

for p in range (1, 5):
    print('------- {} pessoa -------'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ').strip().upper())
    media = idade/4
    soma = soma + media
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    else:
        if idade < 20 and sexo == 'F':
            count = count + 1

print('A média de idade do grupo é {} anos'.format(soma))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(count))