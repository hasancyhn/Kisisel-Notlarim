tr_harfler = "şçöğüı"
parola = input("Parolanız: ")
for karakter in parola:
    if karakter in tr_harfler:
        print("(",karakter,")",sep=",")
    else:
        print(karakter)
