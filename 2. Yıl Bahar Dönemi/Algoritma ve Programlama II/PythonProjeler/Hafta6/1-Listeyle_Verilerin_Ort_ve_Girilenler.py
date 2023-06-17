# Peki girilen sayıların ortalaması ile birlikte
# hangi sayıların girildiğini de göstermek isterseniz
# nasıl bir kod yazarsınız?

sayılar = 0
notlar = []
for i in range(5):
    veri = int(input("{}. not: ".format(i+1)))
    sayılar += veri
    notlar += [veri]
print("Girdiğiniz notlar: ", *notlar)
print("Not ortalamanız: ", sayılar/10)
