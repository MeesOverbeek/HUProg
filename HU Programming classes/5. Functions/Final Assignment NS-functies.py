#the following function calculates the basic formula: standaardTarief
#if the distance traveled is less than 0, the function shall treat standaardTarief as 0 rather than a negative
#the return value given shall now be called "standaardTarief" for further and future usage

def standaardPrijs(afstandKM):
    if afstandKM <= 0:
        afstandKM = 0
    if afstandKM > 50:
        standaardTarief = (afstandKM * 0.60) + 15
    else:
        standaardTarief = afstandKM * 0.80
    return standaardTarief

#this function shall perform the mutations based on the set rules for this assignment

def ritPrijs(leeftijd, weekendrit, afstandKM):
    standaardTarief = standaardPrijs(afstandKM)
#the first line dictates that 'standaardTarief' shall equal the returnvalue of the function standaardPrijs(afstandKM)

#this part checks wether the person enetering the values is of a certain age, either below the age of 12 or age 65 and above
#it checks this through an if else statement
#a second if statement is put in the if statement to ask what day it is, and determine based on the answer if they will get the weekend discount
    if leeftijd >= 65 or leeftijd < 12:
        if weekendrit.lower() == 'zaterdag' or weekendrit.lower() == 'zondag':
            return standaardTarief * 0.65
        else:
            return standaardTarief * 0.70
    else:
        if weekendrit.lower() == 'zaterdag' or weekendrit.lower() == 'zondag':
            return standaardTarief * 0.60

    return standaardTarief

#the value of 'standaardTarief' is returned here

#there are 3 paramaters here, they will get assigned a value based on the input of the user
userAge = int(input('Wat is je leeftijd: '))
traveledDistance = float(input('Hoeveel kilometers heb je afgelegd: '))
isWeekend = input('Welke dag is het vandaag?: ')

#the inputs will be overwritten onto the function's parameters to perform the mutations
#this value shall be calculated and assigned onto 'finalRitprijs'
finalRitprijs = ritPrijs(userAge, isWeekend, traveledDistance)

#a sentence is formed around finalRitprijs and then printed
print('Je ritprijs bedraagd ' + str(finalRitprijs) + ' Euro')

#code works succesfully, assignment closed
