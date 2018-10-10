names = {}

#create an empty dictionary
#create a while loop that will keep asking for inputs, names in this case
#if an empty bit of text is given the programm will end the while loop
while True:
    nameInput = str(input('Volgende naam: '))
    if nameInput == '':
        for name in names:
            print('Er is/zijn {} student(en) met de naam {}'.format(names[name], name))
        break
    elif nameInput in names:
        names[nameInput] += 1
    else:
        names[nameInput] = 1