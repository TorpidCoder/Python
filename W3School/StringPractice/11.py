string = input("enter the string : ")

result = ""


for vals in range(len(string)):
    if(vals%2==0):
        result=result+string[vals]

print(result)
