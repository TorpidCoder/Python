sent = input("enter the string  : ")


if(len(sent)<3):
    print(sent)
elif(sent[-3:]=='ing'):
    print(sent+'ly')
else:
    print(sent+'ing')
