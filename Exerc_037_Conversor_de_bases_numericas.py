numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
# use 3 aspas para fazer várias linhas
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero,bin(numero)[2:]))
# usa-se [2:] porque só quero que apareça da posição 2 até o final - fatiamento de string
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida, tente novamente')

