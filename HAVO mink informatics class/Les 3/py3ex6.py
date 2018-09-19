s = 'Guido van Rossum heeft de programmeertaal Python bedacht'

sentence = s
for letter in sentence:
    if letter in 'aeiouAEIOU':
        print(letter)