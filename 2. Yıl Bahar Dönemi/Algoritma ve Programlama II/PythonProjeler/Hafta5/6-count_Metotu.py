parola = input("Parolanız: ")
kontrol = True
for i in parola:
    if parola.count(i) > 1:
        kontrol = False
if kontrol:
    print('Parolanız onaylandı!')
else:
    print('Parolanızda aynı harfi bir kez kullanabilirsiniz!')

print("\n")

kelime = input("Herhangi bir kelime: ")
sayaç = ""
for harf in kelime:
    if harf not in sayaç:
        sayaç += harf
for harf in sayaç:
    print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf,kelime,kelime.count(harf)))
