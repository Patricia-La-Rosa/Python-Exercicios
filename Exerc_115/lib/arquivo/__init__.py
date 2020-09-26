from Exerc_115.lib.interface import cabecalho

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquivo_criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
#     w escreve, t text, e o +, caso o arquivo não exista ele cria
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo{nome} criado com sucesso')


def arquivoler(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um ERRO ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} feito com sucesso!!! ')
        finally:
            a.close()