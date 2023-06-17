sekil_Secimi = str(input("Şekilin isminiz yazın\n"
                         "Ucgen - Dortgen\n"))

if sekil_Secimi == "Dortgen":
    k1 = int(input("İlk kenar uzunluğunu giriniz:"))
    k2 = int(input("İkinci kenar uzunluğunu giriniz:"))
    k3 = int(input("Üçüncü kenar uzunluğunu giriniz:"))
    k4 = int(input("Dördüncü kenar uzunluğunu giriniz:"))
    if k1 == k2 and k1 == k3 and k1 == k4:
        print("Kare")
    else:
        print("Dörtgen")
elif sekil_Secimi == "Ucgen":
    k1 = int(input("İlk kenar uzunluğunu giriniz:"))
    k2 = int(input("İkinci kenar uzunluğunu giriniz:"))
    k3 = int(input("Üçüncü kenar uzunluğunu giriniz:"))
    if k1 == k2 and k1 == k3:
        print("Eşkenar")
    elif k1 == k3:
        print("İkizkenar")
    elif k1 == k2:
        print("İkizkenar")
    else:
        print("Sıradan üçgen")
else:
    print("Yanlış komut girdiniz.")