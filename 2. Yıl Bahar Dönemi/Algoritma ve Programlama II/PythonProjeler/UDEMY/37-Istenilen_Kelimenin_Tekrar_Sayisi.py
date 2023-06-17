def tekrar(isim):
    tekrar = int(input("İsim kaç kez tekrar etsin?"))
    i = 0
    while i < tekrar:
        print("{}".format(isim))
        i = i+1

tekrar("ali")
