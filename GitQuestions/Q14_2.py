upper = 0
lower = 0

sentence = input("Please enter the string : ")

for val in sentence:
    if(val.isupper()):
        upper+=1
    elif(val.islower()):
        lower+=1


print(upper)
print(lower)
