def guclubul(altlimit, ustlimit):
    def faktoriyel(sayi):
        sonuc = 1
        for i in range(1, sayi+1):
            sonuc = sonuc * i
        return sonuc
    def guclumu(sayi):
        temp = sayi
        basamaklar = []
        while (temp > 0):
            basamak = temp % 10
            basamaklar.append(basamak)
            temp = temp // 10
        toplam = 0
        for i in basamaklar:
            toplam = toplam + faktoriyel(i)
        if (toplam == sayi):
            return True
        else:
            return False
    while(altlimit < ustlimit):
        if(guclumu(altlimit)):
            print(altlimit)
        altlimit = altlimit + 1
guclubul(1, 50000)