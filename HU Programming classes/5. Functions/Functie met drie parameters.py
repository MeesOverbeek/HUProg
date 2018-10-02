def som(getal1, getal2, getal3):
    return getal1 + getal2 + getal3

input1 = eval(input("geef hier de waarde voor het eerste getal: "))
input2 = eval(input("geef hier de waarde voor het tweede getal: "))
input3 = eval(input("geef hier de waarde voor het derde getal: "))

#the three inputvalues are put into the sum given in the defined function
#it is done by replacingthe values of inputs by the values in the same
#position in the original function
print(som(input1, input2, input3))
