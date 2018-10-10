#import the random module
import random

#assign the boundaries of the random integers
def monopolyworp(dubbel):
    worp1 = random.randint(1, 6)
    worp2 = random.randint(1, 6)

#prints the value of both throw 1 and 2, if anyof the conditions below
#is met, a different action shall happen based on said conditions
    if worp1 is worp2 and dubbel == 2:
        print('{} + {} = (direct naar gevangenis)'.format(worp1, worp2))
    elif worp1 is worp2:
        print('{} + {} = {} (dubbel)'.format(worp1, worp2, worp1 + worp2))
        dubbel += 1
        monopolyworp(dubbel)
    elif not worp1 is worp2:
        print('{} + {} = {}'.format(worp1, worp2, worp1 + worp2))

#allows for the function to work
monopolyworp(0)
