toplam = 0
for x in range(100):
    sayi = int(input("Sayı giriniz: "))
    if sayi<0:
        break
    else:
        toplam += sayi
print("\nGirilen sayı adedi: {}".format(x))
print("Ortalama: {}\n".format(toplam/x))
