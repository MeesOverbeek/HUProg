#eval(input()): ask for the amount of points scored
points = eval(input("Geef hier je aantal punten: "))

#if-statement: when amount of points is greater than 15, the participant passed
if points > 15:
    print("Gefeliciteerd!")
    print("Met een score van" + " " + str(points) + " " + "ben je geslaagd")

#else statement: when amount of points is not greater than 15, the particpant has failed the test
else:
    print("Helaas")
    print("Met een score van" + " " + str(points) + " " + "ben je niet geslaagd")
