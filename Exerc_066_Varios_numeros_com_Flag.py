soma = count = 0
while True:
    n = int(input('Digite um valor (999) para parar: '))
    if n == 999:
        break
    count = count + 1
    soma = soma + n
print(f'A soma dos valores foi {soma}')
# nova maneira de usar a string.format