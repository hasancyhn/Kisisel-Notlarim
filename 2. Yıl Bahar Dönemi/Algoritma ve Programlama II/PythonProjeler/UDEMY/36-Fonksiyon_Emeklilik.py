def yasHesapla(dogumYili):
    return 2021 - dogumYili



def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas

    if kalanSure > 0:
        print(f"{isim}, emekliliğinize {kalanSure} yıl kaldı.")
    else:
        print(f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz.")

emekliligeKacYilKaldi(1999, "Hasan")
emekliligeKacYilKaldi(1950, "Memiş")