notunuz = input("notunuz: ")
if not notunuz:
    print("Lütfen notunuzu giriniz!")
    quit()
else:
    notunuz = int(notunuz)
if notunuz not in range(101):
    print("Notunuz 0 ile 100 arasında olmalı")
    quit()
elif notunuz in range(90, 101):
    puan = "AA"
elif notunuz in range(85, 90):
    puan = "BA"
elif notunuz in range(80, 85):
    puan = "BB"
elif notunuz in range(75, 80):
    puan = "CB"
elif notunuz in range(70, 75):
    puan = "CC"
elif notunuz in range(60, 70):
    puan = "DC"
elif notunuz in range(50, 60):
    puan = "DD"
else:
    puan = "FF"
    print("puanınız: ", puan)