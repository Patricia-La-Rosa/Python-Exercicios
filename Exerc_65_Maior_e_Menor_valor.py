n = 0
seg = ''
count = 0
media = 0
soma = 0
maior = 0
menor = 0
# n = count = media = soma = maior = menor = 0 pode-se usar desta maneira
while not 'N' in seg:
    count = count + 1
    n = int(input('Digite um número: '))
    seg = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    soma = soma + n
    media = soma /count
    if count == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

print('Você digitou {} números e a soma foi de {} sendo a média de {:.2f} '.format(count,soma,media))
print('O maior valor foi de {} e o menor foi {}'.format(maior,menor))