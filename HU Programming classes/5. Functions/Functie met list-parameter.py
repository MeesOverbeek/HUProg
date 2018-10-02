def som(getallenLijst):
    totaal = int()
    for getal in getallenLijst:
        totaal += getal
    return totaal
#forces 'totaal' to be displayed as integer
#for-loop asks for a number
#for each next number in the list, it will de added to the previous result (performed by +=)

print(som([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#prints the sum of the given list's numbers as defined by the function