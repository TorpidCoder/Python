def character(char):
    if(char.isupper()):
        print("upper")
    elif(char.islower()):
        print("lower")
    elif(char in ('@ , # , $ , % ,^ ,& , *')):
        print("Special character")
    else:
        print("its a digit")

char = input("Please enter the character : ")

character(char)
