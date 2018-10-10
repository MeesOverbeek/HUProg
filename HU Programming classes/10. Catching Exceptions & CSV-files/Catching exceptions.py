paymentAmount = 4356

#a try-exception error has been put in place OVER an if-loop
#it will divide 2 values, therefore you need 2 values, and the second value can't be 0
#if-loop will prevent anything under 0
#exception errors exist for ZeroDivision and ValueError
#it will also
try:
    amountOfPeople = int(input('Met hoeveel mensen ben je: '))
    if amountOfPeople < 0:
        print('Negatieve getallen zijn niet toegestaan!')
    else:
        print(paymentAmount / amountOfPeople)
except ZeroDivisionError:
    print('Je kan niet delen door nul!')
except ValueError:
    print('Je moet een getal opgeven!')
except:
    print('Onjuiste invoer!')