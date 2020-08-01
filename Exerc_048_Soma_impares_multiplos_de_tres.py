soma = 0
#acumuladores = soma não recebe nenhum número
cont = 0
#contador por enquanto recebe zero porque ele vai indicar quantos numeros foram para se chegar a tal numero
for x in range (1,501,2):
    if x % 3 == 0:
        # formula para ver se é divisível por 3, tem que restar 0
        soma = soma + x
        # soma recebe soma que é 0 + x, que são todos os numeros de x somados (acumula)
        cont = cont + 1
        # conta
print('A soma de todos os {} valores solicitados é {}.'.format(cont,soma))

