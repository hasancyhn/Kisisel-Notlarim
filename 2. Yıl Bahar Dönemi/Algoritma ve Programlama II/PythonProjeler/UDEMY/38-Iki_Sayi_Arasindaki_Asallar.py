# Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if (sayi>1):
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalSayilariBul(10,20)

# Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i ==0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(15))
print(tamBolenleriBul(35))