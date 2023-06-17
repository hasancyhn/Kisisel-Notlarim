# Kendisine verilen sayının Armstrong sayısı olup olmadığını bulan
# fonksiyonu yazınız.

def ar(sayi):
    basamk_Sayisi = len(sayi)
    toplam = 0
    for i in sayi:
        toplam += int(i)**basamk_Sayisi
    if (toplam == int(sayi)):
        print("{} sayısı Armstrong sayısıdır.".format(sayi))
    else:
        print("{} sayısı Armstrong sayısı değildir.".format(sayi))
sayi = input("Sayı giriniz: ")
ar(sayi)