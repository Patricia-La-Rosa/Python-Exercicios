print('GERADOR DE PA')
print('=-'*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
contador = 1

while contador <= 10:
    print('{} -- '.format(termo))
    termo += razao
    contador += 1
print('Fim')
