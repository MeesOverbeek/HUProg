def gemiddelde():
    zin = input('Voer een zin in: ')
    lijst = []
    woorden = []
    nummer = []
#create empty lists
    lijst.append(zin)
#add the input to 'lijst'
#for a 'woord' in 'lijst' it will add it to the list 'woorden' with make-up
    for woord in lijst:
        woorden.append((woord.split(' ')))
#for a 'woord' now in 'woorden' it shall add the length of q to the 'nummer' list
    for woord in woorden:
        for q in woord:
            nummer.append(len(q))
#calculates the average accordingly
    calcAverage = int(sum(nummer)/len(nummer))
    print('de gemmidelde lengte van de woorden in de zin is ' + str(calcAverage))
gemiddelde()