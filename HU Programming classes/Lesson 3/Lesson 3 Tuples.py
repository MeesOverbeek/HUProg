letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')

#this is the current Tuple, immutable

amountA = letters.count('A')
amountB = letters.count('B')
amountC = letters.count('C')

#count all the individual letters in the tuple and assign said value
#to the given variables

occurences = [amountA, amountB, amountC]

#putting all the amount variablees

print(occurences)

#result after printing is [2, 3, 4]