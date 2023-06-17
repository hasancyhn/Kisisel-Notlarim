sys_kullanici = "hassan"
sys_sifre = "123hasan"

kullanici = input("Kullanıcı Adınızı Giriniz: ")
sifre = input("Şifrenizi Giriniz: ")

if (kullanici != sys_kullanici and sifre != sys_sifre):
    print("Kullanıcı Adı ve Şifre Hatalı")
elif (kullanici != sys_kullanici and sifre == sys_sifre):
    print("Kullanıcı Adı Hatalı.")
elif (kullanici == sys_kullanici and sifre != sys_sifre):
       print("Şifre Hatalı.")
else:
    print("Giriş Sağlanıyor, Lütfen bekleyiniz.")

print("Girdiğiniz Kullanıcı Adı: ",kullanici)
print("Girdiğiniz Şifreniz: ",sifre)
print("Sistem Kullanıcı Adı: {}\nSistem Şifresi: {}".format(sys_kullanici, sys_sifre))