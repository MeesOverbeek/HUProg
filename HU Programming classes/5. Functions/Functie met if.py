def langGenoeg(lengte):
    if lengte >= 120:
        return "je bent lang genoeg voor de atractie!"
    else:
        return "Sorry, je bent te klein!"

lengthInput = eval(input("Geef hier je lengte: "))

print(langGenoeg(lengthInput))