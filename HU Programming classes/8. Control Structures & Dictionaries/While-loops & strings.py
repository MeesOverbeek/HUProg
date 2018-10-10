#a simple while loop, when true the if loop will be repeated if conditions are met and no Break
#it asks for a 4 letter string, will execute when given. Else it asks again
user = input('Geef een string van vier letters: ')
while True:
    if len(user) == 4:
        print('inlezen van correcte string: ' + str(user) + ' is geslaagd')
        break
    else:
        print(str(user) + " heeft " + str(len(user)) + " letters")
        user = input('Geef een string van vier letters: ')