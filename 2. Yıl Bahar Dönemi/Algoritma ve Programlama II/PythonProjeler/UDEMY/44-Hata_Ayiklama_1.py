# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

liste = ["1", "2", "a5", "10b", "abc", "10", "50"]
for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except ValueError:
        continue

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazın.

while True:
    sayi = input('sayı: ')
    if (sayi == 'q'):
        break

    try:
        sonuc = float(sayi)
        print(f'girilen sayı: {sonuc}')
        break
    except ValueError:
        print('geçersiz sayı.')
        continue
