
MyString = 'AAAAABBBBAAA'
SecondString = 'Bookkeeping'

def encodeString(input):
    prevChar = None
    counter = 1
    outputlist = []

    for char in input:
        if char != prevChar:
            if prevChar is not None:
                print(f'New character is {char}')
                outputlist.append((prevChar,counter))
            prevChar = char
            counter = 1
        else: 
            counter += 1

    # Add the last group    
    outputlist.append((prevChar, counter))
    return outputlist

print(encodeString(MyString))


SecondString = [('W',5), ('1',2), ('G',2)]


def decodeString(list):

    resultlist = []
    for char, count in list:
        resultlist.append(char * count)
    return ''.join(resultlist)

print(decodeString(encodeString(MyString)))





    
