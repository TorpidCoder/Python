Name = "Sahil nagpal is good boy\tand he is generous"
sum =0
sum_tab = 0
for val in Name:
    if(val==' '):
        sum+=1
    elif(val == '\t'):
        sum_tab+=1



print("The spaces are : ",sum)
print('The tabs are : ',sum_tab)
