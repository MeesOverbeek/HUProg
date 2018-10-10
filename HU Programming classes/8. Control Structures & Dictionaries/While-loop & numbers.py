#very simple while loop, it creates an empty list, which will be filled with the given digits.
#it will keep asking and adding until the user Breaks by entering 0
user = input('Geef een getal: ')
lst = []
while user != '0':
    lst.append(eval(user))
    user = input('Geef een getal: ')
print('Er zijn ' + str(len(lst)) + ' getallen ingevoerd, de som is ' + str(sum(lst)))