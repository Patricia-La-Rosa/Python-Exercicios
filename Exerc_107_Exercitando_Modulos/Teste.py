from Exerc_107_Exercitando_Modulos import Moeda

preco = float(input('Digite o valor: '))
taxa = 10
print(f'A metade de R${preco} é R$ {Moeda.metade(preco)}')
print(f'O dobro do preço de R${preco} é R$ {Moeda.dobro(preco)}')
print(f'O preço de R${preco} com aumento de 10% fica em R$ {Moeda.aumentar(preco,taxa)}.')
print(f'O preço de R${preco} com diminuição de 10% fica em R$ {Moeda.diminuir(preco,taxa)}.')
