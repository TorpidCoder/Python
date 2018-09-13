limit = int(input("Please enter the limit : "))

numbers = []

for vals in range(0,limit):
    numbers.append(int(input("enter the numbers : ")))

odd =[]
even =[]

for vals in numbers:
    if(vals%2==0):
        even.append(vals)
    else:
        odd.append(vals)

odd.sort()
even.sort()

count_even=0
count_odd = 0

for va in odd:
    count_odd+=1
for vao in even:
    count_even+=1

print("Largest number odd: ",odd[count_odd-1])

print("Largest number even : ",even[count_even-1])
