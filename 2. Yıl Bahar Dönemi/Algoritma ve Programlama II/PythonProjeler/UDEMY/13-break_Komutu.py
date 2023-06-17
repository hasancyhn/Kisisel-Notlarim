kullanıcı_adı = "hasan"
parola = "hasan123"
while True:
    soru1 = input("Kullanıcı adı: ")
    soru2 = input("Parola: ")
    if soru1 == kullanıcı_adı and soru2 == parola:
        print("Kullanıcı adı ve parolanız onaylandı.")
        break
    else:
        print("Kullanıcı adınız veya parolanız yanlış.")
        print("Lütfen tekrar deneyiniz!")