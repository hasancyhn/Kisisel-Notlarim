urunler = [
    {'name':'iphone 8', 'price': '4000' },
    {'name':'iphone 8 Plus', 'price': '5000' },
    {'name':'iphone X', 'price': '6000' },
]
# Ürünlerin fiyatları toplamı nedir ?

toplam = 0
for urun in urunler:
    toplam = toplam + int(urun['price'])
print(f'ürün toplamları: {toplam} TL')

# Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz ?
# for urun in urunler:
#     if (int(urun['price']) <= 6000):
#         print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")

# Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.

kelime = input('aramak istediğiniz ürün: ')

for urun in urunler:
    if (urun['name'].find(kelime.lower()) > -1):
        print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")