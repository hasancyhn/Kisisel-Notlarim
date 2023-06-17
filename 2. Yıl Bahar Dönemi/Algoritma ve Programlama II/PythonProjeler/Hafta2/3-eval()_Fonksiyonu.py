print("""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")

veri = input("İşleminiz: ")
hesap = eval(veri)
print(hesap)