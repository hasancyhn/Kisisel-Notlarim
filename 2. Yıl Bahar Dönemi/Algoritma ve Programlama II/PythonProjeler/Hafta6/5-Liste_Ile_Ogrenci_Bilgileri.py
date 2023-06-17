ogr_ad=[]
ogr_numara=[]
ogr_vize_not=[]

ogr_sayisi=int(input("Kaç öğrenciye ait bilgi girilecek: "))

for i in range(ogr_sayisi):

    ad=input("{}.öğrenci adını giriniz: ".format(i+1))
    numara=input("{}.öğrenci  no giriniz: ".format(i+1))
    vizenot=input("{}.vize notunu giriniz: ".format(i+1))
    ogr_ad.append(ad)
    ogr_numara.insert(i,numara)
    ogr_vize_not.append(float(vizenot))

for i in range(ogr_sayisi):
    print("{}.öğrenci  no:{}, adı:{}, vize notu:{}".format(i+1,ogr_numara[i],ogr_ad,vizenot))

print("Vize notu 60'dan büyük olan öğrenciler: ")

for i in range(ogr_sayisi):
    if(ogr_vize_not[i]>60):
        print("{}-{}-{}".format(ogr_numara[i],ogr_ad[i],ogr_vize_not[i]))