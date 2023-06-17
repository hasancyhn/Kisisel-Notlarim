def deneme():
    liste = []
    while True:
        a = input("Giriniz: ")
        if a == "0":
            pass
        elif a == "iptal":
            break
        else:
            liste.append(a)
            print(liste)
deneme()
