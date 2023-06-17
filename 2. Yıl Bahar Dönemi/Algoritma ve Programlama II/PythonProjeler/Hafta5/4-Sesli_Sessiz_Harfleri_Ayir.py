metin = input("Metin giriniz: ")
sesli_Harfler = "aeıioöuü"
sessiz_Harfler = "bcçdfghjklmnprsştyvzwq"
sesli_Metin = ""
sessiz_Metin = ""
harf_Olmayanlar = ""

for i in metin:
    if i in sesli_Harfler:
        sesli_Metin += i
    elif i in sessiz_Harfler:
        sessiz_Metin += i
    else:
        harf_Olmayanlar += i
print("Metinde bulunan sesli harfler: ",end="")
print(*sesli_Metin,sep=", ")
print("Metinde bulunan sessiz harfler: ",end="")
print(*sessiz_Metin,sep=", ")
print("Metinde harf olmayan karakterler: ",end="")
print(*harf_Olmayanlar,sep=", ")