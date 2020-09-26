from datetime import date
trabalho = dict()
now = date.today()
ano = now.strftime('%Y')
trabalho['nome'] = str(input('Nome: '))
trabalho['nasc'] = int(input('Ano de Nascimento: '))
trabalho['CTPS'] = int(input(('Carteira de Trabalho (0 não tem): ')))
trabalho['idade'] = int(ano) - trabalho['nasc']
if trabalho['CTPS'] == 0:
    print('-='*30)
    print(f'- Nome tem o valor {trabalho["nome"]}')
    print(f'- Idade tem o valor {trabalho["idade"]}')
    print(f'- CTPS tem o valor {trabalho["CTPS"]}')
else:
    trabalho['contr'] = int(input('Ano de Contratação: '))
    trabalho['sal'] = int(input('Salário: R$'))
    print('-='*30)
    print(f'- Nome tem o valor {trabalho["nome"]}')
    print(f'- Idade tem o valor {trabalho["idade"]}')
    print(f'- CTPS tem o valor {trabalho["CTPS"]}')
    trabalho['aposent'] = (35 - (int(ano) - trabalho['contr']))+ trabalho['idade']
    print(f'- Contratação tem o valor {trabalho["contr"]}')
    print(f'- Salário tem o valor {trabalho["sal"]}')
    print(f'- Aposentadoria tem o valor {trabalho["aposent"]}')
    # a forma de fazer isso em duas linhas é como está abaixo
    for k, v in trabalho.items():
        print(f'{k} tem o valor {v}')