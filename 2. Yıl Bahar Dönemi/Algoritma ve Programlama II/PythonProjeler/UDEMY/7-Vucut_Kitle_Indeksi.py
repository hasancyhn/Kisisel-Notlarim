boy = float(input("Boyunuzu giriniz: "))
kilo = int(input("Kilonuzu giriniz: "))

beden_Kitle_Indeksi = kilo/(boy**2)

if beden_Kitle_Indeksi<18.5:
    print("Zayıfsınız")
elif beden_Kitle_Indeksi>18.5 and beden_Kitle_Indeksi<25:
    print("Normalsiniz")
elif beden_Kitle_Indeksi>25 and beden_Kitle_Indeksi<30:
    print("Fazla kilolusunuz")
else:
    print("Obezsiniz")