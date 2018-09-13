def found(char, string):
    if char in string:
        return 1
    else:
        return 0    


string = input("enter the string : ")

char = input("enter the character : ")

print(found(char , string))
