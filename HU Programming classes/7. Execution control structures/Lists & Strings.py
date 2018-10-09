lstOld = eval(input('Geef een lijst met minimaal 10 strings op: '))
lst = []
#created an empty list

#if-loop dictates if the list is longer than 10 strings and the length of a word is 4, it shall be printed into the new list
if len(lstOld) >= 10:
    for word in lstOld:
        if len(word) == 4:
            lst.append(word)
    print(lst)
else:
    print('Er is iets mis gegaan, probeer opnieuw')


# ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]