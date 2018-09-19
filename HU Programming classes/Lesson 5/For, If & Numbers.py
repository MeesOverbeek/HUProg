#a basic list of numbers called numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for loop: look for num in numbers
#if: look wether num falls in the set range
#print: prints the outcomeof num
#removal of numbers fro the list will omit them in the printed result as well
for num in numbers:
        if num in range(0, 11, 2):
            print(num)