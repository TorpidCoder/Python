li = []
for val in range(2000,3200):
    if(val%7==0):
        if(val%5!=0):
            li.append(str(val))


print(li)
