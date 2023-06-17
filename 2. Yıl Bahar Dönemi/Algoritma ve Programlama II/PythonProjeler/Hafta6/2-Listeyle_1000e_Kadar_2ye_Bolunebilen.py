

liste = [i for i in range(1000) if i % 2 == 0]
print(liste)

print("\n")

liste2 = []
for i in range(1000):
    if i % 2 == 0:
        liste2 += [i]
print(liste2)