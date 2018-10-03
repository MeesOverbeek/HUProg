import datetime

#ask for a name
name = input('Voer naam in: ')

#this allows manual entering of a date rather than
#hour = int(input('Voer uur in '))
#minute = int(input('Voer minuut in '))
#second = int(input('Voer seconde in '))
#vandaag = datetime.datetime(2016, 5, 10, hour, minute, second)

#vandaag = whatever day it is today
#strftime will allow sorting it neatly into poper display
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %X")
'{}, {}'.format(s, name)
#will perform the actions performed onto the file calles marathon.txt
outfile = open('marathon.txt', 'a')

#it will write it based on the format given below
outfile.write('{}, {}'.format(s, name) + str('\n'))
outfile.close()
#closes file so it can save