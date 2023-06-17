liste1 = [1, 2, 3]
liste2 = ["bir", "iki", "üç"]
print(*zip(l1, l2))

print("\n")

for a, b in zip(liste1, liste2):
    print(a, b)
