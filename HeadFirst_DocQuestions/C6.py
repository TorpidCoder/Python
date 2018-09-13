Name = input("Please enter your number : ")

up_count = sum(map(str.isupper,Name ))

low_count = sum(map(str.islower,Name ))

print("The count of upper is : ",up_count)

print("The count of lower is : ",low_count)
