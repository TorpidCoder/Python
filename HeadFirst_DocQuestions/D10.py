list = []

limit = int(input("Please enter the limit : "))

for val in range(0,limit):

    list.append(int(input("Please enter the number : ")))

print("The list is : ",list)

sum_neg = 0
sum_pos = 0
sum_odd = 0
sum_eve = 0

for val_neg in list:
    if(val_neg<0):
        sum_neg+=1

for val_pos in list:
    if(val_pos>0):
        sum_pos+=1

for val_eve in list:
    if(val_eve%2==0):
        sum_eve+=1

for val_eve in list:
    if(val_eve%2!=0):
        sum_odd+=1


print("The values of negative numbers are : " , sum_neg)

print("The values of positive numbers are : " , sum_pos)

print("The values of even numbers are : " , sum_eve)

print("The values of odd numbers are : " , sum_odd)
