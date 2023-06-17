import datetime

tarih = input('Aracınız hangi tarihte trafiğe çıktı? (2019/7/11)\n')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

print(gun)

if (gun<= 365):
    print('1.servis bakımı.')
elif (gun>365) and (gun<=365*2):
    print('2.servis bakımı')
elif (gun>=365*2) and (gun<=365*3):
    print('3.servis bakımı')
else:
    print('hatalı bilgi girdiniz.')