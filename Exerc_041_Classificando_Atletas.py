from datetime import date
ano = int(input('Digite o ano que você nasceu: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('De acordo com a sua idade de {} anos sua categoria é MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('De acordo com a sua idade de {} anos sua categoria é INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('De acordo com a sua idade de {} anos sua categoria é JUNIOR'.format(idade))
elif idade > 19 and idade <=25:
    print('De acordo com a sua idade de {} anos sua categoria é SÊNIOR'.format(idade))
else:
    print('De acordo com a sua idade de {} anos sua categoria é MASTER'.format(idade))



