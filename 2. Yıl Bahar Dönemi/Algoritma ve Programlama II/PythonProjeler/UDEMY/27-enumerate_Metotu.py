isimler = ["ahmet", "ışık", "ismail", "çiğdem"]
print(*enumerate(isimler))

for sıra, öğe in enumerate(isimler):
    print(sıra, öğe)

print("\n")

for sıra, öğe in enumerate(isimler, 1):
    print(sıra, öğe)