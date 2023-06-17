# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

sayilar = []
i = 0
while (i<5):
    sayi = int(input('Sayı: '))
    sayilar.append(sayi)
    i += 1

sayilar.sort()
print(sayilar)
