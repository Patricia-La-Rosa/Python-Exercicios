a = float(input('Digite uma distância em metros: '))
km = a / 1000
hm = a / 100
dam = a / 10
dm = 1 * 10
cm = 1 * 100
mm = a * 1000
print('A medida de {}m corresponde a \n {}km \n {} hm \n {} dam \n {}dm \n {}cm \n {}mm'.format(a,km,hm,dam,dm,cm,mm))
