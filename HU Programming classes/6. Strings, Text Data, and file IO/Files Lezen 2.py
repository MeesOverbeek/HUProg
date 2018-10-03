def counting(file):
    Inhoud = open(file, 'r')
    reader = Inhoud.read()
    print('Deze file heeft ' + str(reader.count('\n') + 1) + ' regels')
    Inhoud.close()
#first part opens the file, reads it, counts the amount of lines and puts them in the sentence and prints it
    Inhoud = open(file, 'r')
    Lijst = []
    numbers = []
#creates 2 empty lists and opens the file (given at the bottom)
    reader = Inhoud.readlines()
    for nummer in reader:
        Lijst.append(nummer.strip().split(','))
    for nummer in Lijst:
        numbers.append(nummer[0])
#contents are opened, for a 'nummer' in reader it will be added to
#the empty list will be added a value from 'number' and will split it according to make-up
#for a 'nummer' in 'Lijst' it will add a number to the list
    maximumNumber = max(numbers)
    lineNumber = numbers.index(max(numbers)) + 1
#this will have defined the functions performed at maximumNumber and lineNumber
    print('Het grootste kaartnummer is ' + str(maximumNumber) + ' op regel ' + str(lineNumber))
counting('kaartnummer.txt')
#finally, the outcome of the maximum number and line number are put into a sentence in a forced string format
#the function will be executed with the file 'kaartnummer.txt'
