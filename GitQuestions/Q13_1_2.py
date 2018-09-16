words = input("enter the words : ")

dict = {"digits":0 , "letters":0}

for vals in words :
    if vals.isalpha():
        dict["letters"]+=1
    if vals.isdigit():
        dict["digits"]+=1


print("The letters are : " ,dict["letters"])

print("The digits are : " ,dict["digits"])
