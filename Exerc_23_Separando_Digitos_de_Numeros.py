num = int(input('Digite um número: '))
# preciso transformar de inteiro para string para poder indicar a posição que quero
# n = str(num)
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(n[3]))
# print('Dezena: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))
# desta maneira não consigo fazer corretamente por exemplo para números que não tenham milhares

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
# dividi-se o número por 1 e o que resta por dez (confirmar informação com a Jeje)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format (d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))