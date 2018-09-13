def find(arr , string):
    if(string in arr):
        return "Present"
    else:
        return "not present"

arr =[]

size = int(input("Please enter the limit : "))

for vals in range(0,size):
    arr.append(input("Please enter the words : "))


print("The array is : " , arr)

string = input("Please enter the string 1 : ")

print(find(arr,string))
