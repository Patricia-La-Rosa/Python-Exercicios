nome = str(input('Digite seu nome: ')).strip()
# o strip é para retirar os espaços adicionais
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
# o - nome. count é para tirar o espaço do meio do nome, para poder contar corretamente o numero de letras
div = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(div[0],len(div[0])))
