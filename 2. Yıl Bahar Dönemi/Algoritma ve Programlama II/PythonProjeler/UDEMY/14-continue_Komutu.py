while True:
    sayi = input("Bir sayı girin: ")
    if sayi == "iptal":
        break
    elif len(sayi) <= 3:
        continue
    print("En fazla üç haneli bir sayı girin.")