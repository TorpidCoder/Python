val = input("Enter something : ")
valid_symbols = "!@#$%^&*()_-+={}[]"

if(val.isdigit()):
    print("its a digit")
elif(val.islower()):
    print("its a lower letter")
elif(val.isupper()):
    print("its a upper letter")



for values in val :
    if(values in valid_symbols):
        print("its a symbol")

check = [x for x in val if not x.isupper() and not x.islower()]
print("This is combi")
