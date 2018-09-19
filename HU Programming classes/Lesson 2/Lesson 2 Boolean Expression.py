#assigning values
voornaam = 'Mees'
tussenvoegsel = 'D'
achternaam = 'Overbeek'

#assigning different strings to value 'mijnnaam'
mijnnaam = str(voornaam) + str(tussenvoegsel) + str(achternaam)



#a < 75 < b

#print the length of each individual previously defined string
print(len(voornaam) + len(tussenvoegsel) + len(achternaam) == len(mijnnaam))

#print: is the legth of "mijnnaam" equal to the lengtht of "tussenvoegsel" * 5, true or false
print(len(mijnnaam) == len(5 * tussenvoegsel))

#print wether "tussenvoegsel" is in "achternaam", true or false
print(tussenvoegsel in achternaam)