print('=' * 12,'LOJAS GUANABARA','='* 12)
preco = float(input('Qual o preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
n1 = preco - (preco * 10 / 100)
n2 = preco - (preco * 5 / 100)
n3 = preco
n4 = preco + (preco * 20 / 100)
print(' [1] à vista, dinheiro ou cheque \n [2] à vista cartão \n [3] 2x no cartão \n [4] 3x ou mais no cartao')
pg = int(input('Qual a sua opção para pagamento? '))
if pg == 1:
    print('Sua compra de R$ {:.2f}, com pagamento à vista em dinheiro ou cheque'.format(preco), end=' ')
    print('terá um desconto de 10%, sendo o valor a de pagar R$ {:.2f}'.format(n1))
elif pg == 2:
    print('Sua compra de R$ {:.2f}, com pagamento à vista no cartão'.format(preco), end=' ')
    print(' terá um desconto de 5%, sendo o valor a pagar R$ {:.2f}'.format(n2))
elif pg == 3:
    print('O valor para pagamento de sua conta foi de R$ {:.2f}, sendo parcelada em 2x no cartão'.format(n3))
elif pg == 4:
    prz = int(input('Quantas parcelas? '))
    if prz == 0 or prz == 1 or prz == 2:
        print('Este parcelamento não é permitido, escolha o parcelamento em 3x ou mais', end=' ')
        print('ou retorne para a opção 3 para escolher pagamento em 2x')
    else:
        print('Sua compra de R$ {:.2f}, com parcelamento em {}x, terá um acréscimo de 20% de juros'.format(preco,prz), end= ' ')
        print('e o valor a pagar é R$ {:.2f}'.format(n4))
