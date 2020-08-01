frase = str(input('Digite uma frase: ')).strip().upper()
#uso o strip para tirar os espaços antes e depois da frase
#uso o upper para colocar tudo em maiuscula
palavras = frase.split()
#uso o split para dividir a frase em palavras
junto = ''.join(palavras)
#uso o Join para juntar tudo
# print('Você digitou a frase {}.'.format(junto))
inverso = ''
#dou um valor vazio para o inverso
for letra in range (len(junto) - 1, -1, -1):
#uso o len para saber quantos carateres tenho e + 1 para acabar na última letra
#ele vai pegar o número de letras do junto
    inverso += junto[letra]
print(junto,inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um Palindromo')




