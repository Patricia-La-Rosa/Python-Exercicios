from Exerc_112_ValidandoDinheiro.utilidades import moeda
from Exerc_112_ValidandoDinheiro.utilidades import dados

preco = dados.leiadinheiro('Digite o valor: ')
moeda.resumo(preco, taxaa = 10, taxar=5)
