maas = int(input("Maaşınızı Giriniz"))
cocukSayisi = int(input("Çocuk Sayısını Giriniz: "))
oncekZam = float(input("Önceki Zam Miktarını Giriniz: "))

if maas<3000:
    yeniZam = 0.2
elif maas<4000:
    yeniZam = 0.15
else:
    yeniZam = 0.1

yeniMaas = (maas*yeniZam) + (cocukSayisi*70) + maas
oncekiMaas = maas + oncekZam
if yeniMaas<oncekiMaas:
    oncekiMaas = yeniMaas

print("{}".format(yeniMaas))