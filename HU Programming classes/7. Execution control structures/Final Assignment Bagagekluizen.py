#funtion to show which lockers are open/free
#creates an empty list to edit with
#opens and reads the 'reader' --> 'kluizen.txt'
#if the 'kluis1' is in the file and it's not empty space, it will add 'kluis1' to the list
#'vrij_YN' shall take the number 12 (max locker number) and substract the amount of lockers
#it will print the amount, which will be remaining open lockers
def toonAantalKluizenVrij():
    list1 = []
    inhoud = open('kluizen.txt')
    reader = inhoud.readlines()
    for kluis1 in reader:
        if kluis1 != '\n':
            list1.append(kluis1.strip().split(';'))
    vrij_YN = 12 - len(list1)
    print('Er zijn ' + str(vrij_YN) + ' kluisjes vrij')

#an empty list is created
#it will show which lockers are in use by adding it to 'vol_YN'. a sentence is printed which shows the stripped list vol_YN
#this list contains the lockers in use
    vol_YN = []
    kluisnummers1 = []
    for kluis1 in list1:
        kluisnummers1.append(int(kluis1[0]))
    for kluis1 in kluisnummers1:
        if kluis1 in kluisnummers1:
            vol_YN.append(kluis1)
    print("De kluisjes/het kluisje- " + str(vol_YN).strip("[").strip("]") + " -is/zijn bezet.\n")

#function which grants you your new locker
#it will check which lockers are full and will act upon that in a similair way to the previous function
def nieuweKluis():
    list2 = []
    kluisnummer2 = []
    vol_YN =[]
    content = open('kluizen.txt', 'r')
    reader = content.readlines()
    for kluis2 in reader:
        if kluis2 != '\n':
            list2.append(kluis2.strip().split(';'))
    for kluis2 in list2:
        kluisnummer2.append(int(kluis2[0]))
    for kluis2 in kluisnummer2:
        if kluis2 in kluisnummer2:
            vol_YN.append(kluis2)
    print("De kluisjes " + str(vol_YN).strip("[").strip("]") + " zijn bezet.")
    content.close()
#a multitude of elifs is made here to check the conditions required to get a new locker
    nummer = int(input('Voer een kluisnummer in '))
    if len(kluisnummer2) == 12:
        print('Er zijn geen kluisjes meer vrij\n')
        nieuweKluis()
    elif nummer in kluisnummer2:
        print('Dat kluisje is bezet\n')
        nieuweKluis()
    elif nummer not in kluisnummer2 and nummer <13 and nummer > 0:
        code = input('Voer een kluiscode in ')
        content = open('kluizen.txt','a')
        content.write(str('\n')+'{};{}'.format(nummer, code))
        print('U heeft kluisje ' + str(nummer)+' gekregen\n')
    elif nummer > 12:
        print('Er zijn maar 12 kluisjes\n')
        nieuweKluis()
    elif nummer < 0:
        print('U kunt geen negatieve kluisjes opgegven\n')

#allows you to open your locker with correct password
#it creates a function and an empty list. it will also create multiple input parameters
#if the input corresponds with any of the given conditions, the following action shall be executed
def kluisOpenen():
    list3 = []
    kluisNummerInput = input('Voer een kluisnummer in: ')
    code = input('Voer uw code in: ')
    content = open('kluizen.txt')
    reader = content.readlines()
    content.close()
    for x in reader:
        list3.append(x.strip().split(';'))
    for x in list3:
        if kluisNummerInput == x[0] and code == x[1] and 12 >= int(kluisNummerInput):
            stop = print('U kunt het kluisje openen\n')
            return stop
        elif int(kluisNummerInput) > 12:
            print('Er zijn maar 12 kluisjes')
            break
    else:
        print('Wachtwoord en kluisnummer komen niet overeen\n')

#a while True loop has been put into place to prerform the different actions until the break is given
while True:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil toegang tot mijn klas\n4: Sluit af')
    userInput = input('Maak uw keuze ')
    if userInput == '1':
        toonAantalKluizenVrij()
    elif userInput == '2':
        nieuweKluis()
    elif userInput == '3':
        kluisOpenen()
    elif userInput == '4':
        break
    else:
        print('U kunt maar tussen 1 tot en met 4 kiezen\n')
#h