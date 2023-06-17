vize = int(input("Vize Notunu Giriniz: "))
final = int(input("Final Notunu Giriniz: "))
ortalama = ((vize*0.40)+(final*0.60))
gecmeNotu = 59.45
if ortalama>gecmeNotu:
    print("Tebrikler {} ortalama ile dersi geçtiniz.".format(ortalama))
else:
    print("Malesef başaramadınız.")