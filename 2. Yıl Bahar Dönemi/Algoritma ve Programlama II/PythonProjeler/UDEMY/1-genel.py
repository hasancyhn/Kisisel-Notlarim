

def bolme(x,y):
    print("Bölme fonks. girildi.")
    bol = x/y
    print("Bölme fonks. çıkıldı.")
    return bol
try:
    print("Bölme fonks. öncesi.")
    print(bolme(5, 0))
    print("Bölme fonks. sonrası.")
except ZeroDivisionError:
    print("0'a bölme hatası.")
except ValueError:
    print("Geçersiz değer girildi.")
except:
    print("Bilinmeyen hata oluştu.")





""



































