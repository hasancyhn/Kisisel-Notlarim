# Kullanıcı tarafından girilen web site url’sinin sadece domain
# kısmını ekranda gösteren Python kodunu yazınız.

# http://www.huseyinhakli.com
url = input("URL giriniz: ")
print(url[11:-4])

# http//:wwww.oyak.gov
url = input("URL giriniz: ")
print(url[12:-4])