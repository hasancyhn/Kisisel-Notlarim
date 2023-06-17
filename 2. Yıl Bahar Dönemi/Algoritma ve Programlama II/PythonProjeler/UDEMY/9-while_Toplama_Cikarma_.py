while True:
 seçenek1 = "(1) toplama"
 seçenek2 = "(2) çıkarma"
 print(seçenek1)
 print(seçenek2)
 soru = input("Yapılacak işlemin numarasını girin: ")
 if soru == "1":
    sayı1 = int(input("Toplama için ilk sayıyı girin: "))
    sayı2 = int(input("Toplama için ikinci sayıyı girin: "))
    print(f"{sayı1} + {sayı2} = {sayı1 + sayı2}")
 if soru == "2":
    sayı3 = int(input("Çıkarma için ilk sayıyı girin: "))
    sayı4 = int(input("Çıkarma için ikinci sayıyı girin: "))
    print(f"{sayı3} - {sayı4} = {sayı3 - sayı4}")