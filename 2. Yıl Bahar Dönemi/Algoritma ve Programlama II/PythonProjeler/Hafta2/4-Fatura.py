ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
subat = 28
nisan = haziran = eylul = kasim = 30
ay = input("Hangi aya ait faturayi istiyorsunuz?")
ay = eval(ay);
subirimfiyati = float(input("Suyun birim fiyatini giriniz: "))
kullanim = float(input("Toplam tuketilen metrekup miktarini giriniz: "))
gunluktutar = (kullanim/ay)*subirimfiyati
ayliktutar = gunluktutar*ay
print("günlük tutar = {:.2f},aylık tutar ->{:.5f}".format(gunluktutar, ayliktutar))
print("günlük tutar = {},aylık tutar ->{:.2f}".format(gunluktutar, ayliktutar))
print(f"günlük tutar {gunluktutar} aylık tutar {ayliktutar}")
# 10. satır = 11. satır = 12. satır !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
