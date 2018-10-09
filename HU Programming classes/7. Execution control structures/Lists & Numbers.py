invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

#create variables for each assignment that has to be performed
numbers = invoer.split('-')
numbers.sort()
maximum = max(numbers)
minimum = min(numbers)
count = len(numbers)
#use a for loop to calculate the sum of the numbers
som = int()
for x in numbers:
    som += int(x)
average = som / count
print('Gesorteerde list van ints: ' + str(numbers))
print('Grootste getal: ' + str(maximum) + ' en het Kleinste getal ' + str(minimum))
print('Aantal getallen: ' + str(count) + ' en Som van de getallen: ' + str(som))
print('Gemiddelde: ' + str(average))