def kwadratenSom(grondGetallen):
    totalSom = int()
    for getal in grondGetallen:
        if getal > 1:
            totalSom += getal**2
    return totalSom

print(kwadratenSom([4, 5, 3, -81]))
print(kwadratenSom([7, 15, -43, -81]))
print(kwadratenSom([14, -5, 3, -81]))
print(kwadratenSom([-4, -5, -8, -81]))