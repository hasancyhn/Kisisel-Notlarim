parola = input("Şifrenizi giriniz: ")
kontrol = None

for i in range(10):
    if parola.startswith(str(i)):
        print("Şifre rakam ile başlayamaz.")
        kontrol = 1
        break
    if parola.endswith(str(i)):
        print("Şifre rakam ile bitemez.")
        kontrol = 1
        break
if kontrol is None:
    print("Şifre başarı ile oluşturuldu.")