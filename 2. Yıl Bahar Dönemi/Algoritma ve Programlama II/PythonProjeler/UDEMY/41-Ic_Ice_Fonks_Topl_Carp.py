def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,3,5,6,7))

carpma = islem("carpma")
print(carpma(1,2,3,6,4))