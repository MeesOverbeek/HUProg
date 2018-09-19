#defining the hourly wage and th =e amount of hours worked
#asked for input to get the values
#eval evaluates wether the input is a string or an integer/float/whatever
hourWage = eval(input("Wat verdien je per uur?: "))
hourWorked = eval(input("hoeveel uur heb je gewerkt?: "))

#basic formula to get the amount of money recieved
payCheque = hourWage * hourWorked

#make the message that the user will see with their data
message = str(hourWorked) + " uur werken levert " + str(payCheque) + " Euro op"

#print the message
print(message)