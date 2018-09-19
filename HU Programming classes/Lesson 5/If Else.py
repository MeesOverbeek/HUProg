#eval(input()): ask for the age of this person
age = int(input("Geef hier je leeftijd: "))

#eval(input()): as wether the person owns a Dutch passport
nationality = str(input("Heeft u een nederlands paspoort?: "))

#if-statement: when amount of points is greater than 15, the participant passed
if age >= 18 and (nationality == 'ja' or nationality =='Ja'):
    print("Gefeliciteerd, U mag stemmen!")

#else statement: if the Person has no Dutch passport or is 18 or older, the person is disallowed to vote
#this else statement is part of the exercise: Lesson 5 IfElse/else
else:
    print("Helaas, U mag niet stemmen.")