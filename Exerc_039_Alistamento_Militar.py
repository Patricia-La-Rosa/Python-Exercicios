from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano

print('Quem nasceu em {} tem anos {} em {}.'.format(ano,idade,atual))
if idade < 18:
    print('Ainda não é momento de você se alistar')
elif idade > 18:
    print('Voce já deveria ter se alistado à {} anos.'.format(idade - 18))
    print('Seu ano de alistamento foi em {}.'.format(ano + 18))
else:
    print('Você deve se alistar IMEDIATAMENTE')

