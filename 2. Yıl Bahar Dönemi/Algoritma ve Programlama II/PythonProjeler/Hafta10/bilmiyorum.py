"""
def karsilik_bul(*args, **kwargs):
    for sozcuk in args:
        if sozcuk in kwargs:
            print("{} = {}".format(sozcuk, kwargs[sozcuk]))
        else:
            print("{} kelimesi sözlükte yok!".format(sozcuk))
sozluk = {"kitap"       : "book",
          "bilgisayar"  : "computer"}
karsilik_bul("kitap", "bilgisayar", "programlama", "fonksiyon", **sozluk)



"""

def bas(*args, start="", **kwargs):
    for oge in args:
        print(start+oge, **kwargs)
f = open("te.xt", "w")
bas("oge1", "oge2", "oge3", start="#.", end="", file=f)