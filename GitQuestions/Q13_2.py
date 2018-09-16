words = input("enter the words : ")

digit = 0

letters =0

for vals in words.split(' '):
    if(vals.isdigit()):
        digit+=1
    elif(vals.isalpha()):
        letters+=1
    else:
        pass


print("The count of digits are : " ,digit)

print("The count of letters are : " , letters)
