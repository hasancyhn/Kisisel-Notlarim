metin = input("Metin girin: ")
aranacak = input("Aradığınız harf: ")
for i in range(len(metin)):
    if i == (metin.index(aranacak, i)):
        print(i)

