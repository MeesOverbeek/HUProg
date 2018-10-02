def kwadratenSom(grondGetallen):
    totalSom = int()
    for getal in grondGetallen:
        if getal > 0:
            totalSom += getal**2
    return totalSom

#totalSom will be given as integer
#if 'getal' is in 'grondGetallen' it will add the next value of
#the given list to the next step
#it will only do this if the number is greater than 0
#0^2 will remain 0, so it has been omitted in the calculations
#totalSom will add the power of the next number to the sum of the given list

#multiple examples have been written down here to give a showcase
print(kwadratenSom([4, 5, 3, -81]))
print(kwadratenSom([7, 15, -43, -81]))
print(kwadratenSom([14, -5, 3, -81]))
print(kwadratenSom([-4, -5, -8, -81]))
print(kwadratenSom([0, 1, 5, -81]))