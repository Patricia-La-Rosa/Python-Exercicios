from Exerc_115.lib.interface import *
from time import sleep
from Exerc_115.lib.arquivo import *

arq = 'nome.txt'

if not arquivoExiste(arq):
    arquivo_criar(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        arquivoler(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        sleep(1)
        print('Saindo do Sistema... Até logo.')
        break
    else:
        print('\33[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)