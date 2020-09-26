from urllib import request

try:
    site = request.urlopen('http://www.pudim.com.br')
except:
    print("Deu erro")
else:
    print('O site está no ar')
    print(site.read(),end='')
    #o site.read é para pegar o código html do site
