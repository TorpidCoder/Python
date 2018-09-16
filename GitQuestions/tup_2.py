tuppy = (1,2,3,4,5,6,7,8,9,10)

li =[]

for vals in tuppy:
    if(vals%2==0):
        li.append(vals)


print("The tuple is : ",tuple(li))
