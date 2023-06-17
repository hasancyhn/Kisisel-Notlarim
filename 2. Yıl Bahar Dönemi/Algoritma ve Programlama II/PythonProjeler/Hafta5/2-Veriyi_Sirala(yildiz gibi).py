# Kullanıcıdan alınan stringi sırayla her seferinde
# tek karakter ekleyerek ekranda gösteren Python
# kodunu yazınız.

mesaj = input("İsim giriniz: ")

for i in range(len(mesaj)):
    print(mesaj[0:i+1])