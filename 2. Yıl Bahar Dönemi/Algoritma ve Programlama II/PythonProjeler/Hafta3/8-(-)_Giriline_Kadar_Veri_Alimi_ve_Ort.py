# Kullanıcıdan negatif sayı girilene kadar sayı alan ve
# bu sayıların ortalamasını veren kodu yazınız.

sayi = int(input("Sayı giriniz: "))
toplam = 0
sayac = 0
while sayi >= 0:
    toplam += sayi
    sayi = int(input("Sayı giriniz: "))
    sayac += 1
if sayac != 0:
    print(toplam/sayac)