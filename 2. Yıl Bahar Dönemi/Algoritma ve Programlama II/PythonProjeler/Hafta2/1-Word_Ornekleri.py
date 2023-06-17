print("Merhaba Akif")
print('Merhaba Akif')
print('''Merhaba Hasan''')

# print("Elif, "Kırıkkale'ye gidiyorum." dedi")     YANLIŞ
print("Elif, \"Kırıkkale'ye gidiyorum\" dedi")      #DOĞRU
print("Merhaba Zalim Dünya", end="**\n")

ad="Hasan"
soyad='CEYHAN'
print(f"{ad=}, {soyad=}")

print("bin" + "beş" + "yüz")

print("Yaşınız:", 23)

# print(2 2)                                        YANLIŞ
print(2 + 2)                                    #   DOĞRU

print("www", "google", "com", sep=".")
print("afyon", "kara", "hisar", sep='') # sep'de boşluk yok
print(*"istihza")
print(*"istihza", sep="/")
print(*"Türkiye", *"Büyük", *"Millet", *"Meclisi", sep=".")
# print(*12345)                                 #   YANLIŞ

print("Merhaba Zalim Dünya", end="**\n")

print(2**3)
print(9%2)

a=3
b=10
print(a, "ile", b, "sayılarını çarparsak", a * b, "elde ederiz.")
print(f"{a} ile {b} sayılarını çarparsak {a * b} elde ederiz.")
print(f"{a} sayısı {b} sayısından büyüktür")

ad="Elif"
soyad="Tükettin"
print(f"{ad=}, {soyad=}")

print(f"4 * 4 = {4 * 4}")


birinci, ikinci = "Python", "Java"
print(birinci)
print(ikinci)
birinci, ikinci = ikinci, birinci
print(birinci)
print(ikinci)

isim = input("adınızı giriniz ->")
print(type(isim))

print(bool(-5))

print("""Algoritma
        ve
        Programlama""")

print("Cim"+"Bom"*3)
print("{0} {1} ({1} {0})".format("Fırat", "Özgül"))