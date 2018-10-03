def convert(temparatuur):
    return temparatuur * 1.8 + 32
#function which will convert a given value --> it will do so by multiplying the given value by 1.8 and adding 32 to it

#a function to create the table
#it will call on the previous function and calculate the value it has to show
#it will print it according to the given make-up
#it will keep printing different calculations, as long as it remains in the given range

def tabel():
    print('  C\t\t\tF')
    for temp in range(-30, 41, 10):
        Farenheit = convert(temp)
        print('{:3}{:11}'.format(temp, Farenheit))
tabel()
