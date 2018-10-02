def langGenoeg(lengte):
    if lengte >= 120:
        return "je bent lang genoeg voor de atractie!"
    else:
        return "Sorry, je bent te klein!"

#created a function with an if-loop
#if given length is equal or greater than 120, the function will return True
#if ther person is less than 120, the function will return false
#this function would allow someone 20m in length to go on the ride
#realistically, a cap should be set

lengthInput = eval(input("Geef hier je lengte: "))
#the input required for the function to be executed
#an evalutaion is put in place to check wether the asked value shall be
#displayed as an integer or something else

print(langGenoeg(lengthInput))