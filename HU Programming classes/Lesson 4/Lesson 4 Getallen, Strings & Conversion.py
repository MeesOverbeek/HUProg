#these are the given grades for the different courses
#could be changed to inputs to ask for the person's grades
cijferICOR = 8
cijferPROG = 7
cijferCSN = 6

#the 3 course grades are added and divided by 3 to give the course average
gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3

#the reward given is calculated here
#this is done through multiplaying the average grade by 30 to get the average reward for 1 class
#multiplying by 3 again gives the average total reward for all 3 courses
beloning = (gemiddelde * 30.0 * 3.0)

#a sentence is built to display the correct message and reward
overzicht = 'mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') levert een beloning van €' + str(beloning) + ' op!'

print(overzicht)