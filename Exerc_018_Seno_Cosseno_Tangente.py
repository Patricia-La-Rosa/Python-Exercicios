import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,tg))

# Por ser em ingles, o retorno de seno e cosseno é em 45 graus, por isso devemos usar o radiano, para ajustar para o Brasil