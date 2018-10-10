#a function has been created to perform both functions
#the file is opened and shall be read only
#an emtpy dic is created to put the data in
#this dictionary gets printed to show your options
def ticker(filename):
    content = open(filename, 'r')
    reader = content.readlines()
    list1 = []
    for ticker in reader:
        list1.append(ticker.strip().split(':'))
    dic = {}
    for ticker in list1:
        key = ticker[0]
        value = ticker[1]
        dic[key] = value
    print(dic)

#this for-loop reads the input and gives the output on the other side of the given index
#if a Ticker is given, a company shall be printed
#if a company is given, a Ticker shall be printed
#this is done through a for-loop, if it is a company it shall show a ticker and vice versa
    list2 = []
    for ticker in dic.values():
        list2.append(ticker)
    company = input('Enter company name: ')
    if company in dic:
        print(dic[company])
    elif company not in dic:
        for ticker, y in dic.items():
            if y == company:
                print("Ticker Symbol: " + ticker)
ticker('ticker.txt')

#previous code copied and replaced input text.
def ticker2(filename):
    content = open(filename, 'r')
    reader = content.readlines()
    list1 = []
    for ticker in reader:
        list1.append(ticker.strip().split(':'))
    dic = {}
    for ticker in list1:
        key = ticker[0]
        value = ticker[1]
        dic[key] = value
    print(dic)

    list2 = []
    for ticker in dic.values():
        list2.append(ticker)
    company = input('Enter Ticker Symbol: ')
    if company in dic:
        print(dic[company])
    elif company not in dic:
        for ticker, y in dic.items():
            if y == company:
                print("Company name: " + ticker)
ticker2('ticker.txt')