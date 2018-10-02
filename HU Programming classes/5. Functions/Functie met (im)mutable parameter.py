lijst = ['a', 'b', 'c']

def wijzig(letterLijst):
    lijst.clear()
    lijst.append('d')
    lijst.append('e')
    lijst.append('f')

#'lijst' will be printed, it will show [a, b, c]
#after this the function 'wijzig' will be executed
#it will clear the list and add the letters 'd, e, f'
#it will then print the list again

print(lijst)
wijzig(lijst)
print(lijst)

#de opdracht lijst = [d, e, f] werkt niet omdat
#de code werkt niet met een string parameter
#er ontstaat een Syntax Error
#mutibaliteit is hier essentieel, aangezien je een
#list aanpast. een tuple zou je niet aan kunnen passen

