print('='*20)
print('10 TERMOS DE UMA PA')
print('=' *20)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão de uma PA: '))
decimo = primeiro + (10 -1) * razao
# fórmula para saber o décimo número de uma progressão aritmética

for c in range (primeiro, decimo, razao):
    print ('{}'.format(c), end=' ')
print('ACABOU')