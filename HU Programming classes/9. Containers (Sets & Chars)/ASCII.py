#define functions based on given parameters
#create an empty string

def code(string):
    string = list(string)
    asciiString = list()
    newString = ''
#for a given characters, ord(char)+3 makes it advance 3 ascii places
    for char in string:
        asciiString.append(ord(char) + 3)
#adds the given result to newString
    for char in asciiString:
        newString += chr(char)

    return newString

print(code('RutteAlkmaarDen Helder'))