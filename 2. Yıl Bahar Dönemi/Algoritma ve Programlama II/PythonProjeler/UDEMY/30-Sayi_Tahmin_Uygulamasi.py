import random

sayi = random.randint(1,20)
hak = int(input("Kaç hak kullanmak istersiniz?  "))
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(f"Tebrikler {sayac}. defada bildiniz.")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Asağı")
    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")