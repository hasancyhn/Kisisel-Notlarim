# dosya = open("deneme2.txt", "w")
# dosya.write("Alg. ve Prog.-2\n")
# dosya.close()


# dosya = open("deneme2.txt", "a")
# dosya.write("Programlama Dillerinin Kavramları")
# dosya.close()

dersler = ["Alg. ve Prog-2", "Programlama Dillerinin Kavramları", "Matematik"]
dosya = open("dersler.txt", "a")
for ders in dersler:
    dosya.write(ders + "\n")
yeniders = input("Yeni ders ismi:")
dosya.write(yeniders)
dosya.close()