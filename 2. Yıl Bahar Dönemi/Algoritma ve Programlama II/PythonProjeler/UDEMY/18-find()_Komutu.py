# 6- urunler listesinde içinde 'iphone' geçen kaç
#  ürün vardır? (index,find)

urunler = ['iphone 8','iphone 7','iphone X','iphone XR','samsung S10']

count = 0
for urun in urunler:
    index = urun.find('iphone')
    if (index>-1):
        count += 1
print(count)