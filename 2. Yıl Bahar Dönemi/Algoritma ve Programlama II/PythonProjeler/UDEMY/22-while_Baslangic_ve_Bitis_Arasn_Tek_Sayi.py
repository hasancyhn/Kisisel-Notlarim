# Başlangıç ve bitiş değerlerini kullanıcıdan alıp
# arada kalan tüm tek sayıları ekrana yazdırın.

baslangic = int(input('Başlangıç: '))
bitis = int(input('Bitiş: '))

i = baslangic

while i < bitis:
    i += 1
    if (i%2==1):
        print(i)