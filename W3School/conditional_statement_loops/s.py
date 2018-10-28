row=15
col=18
result_str=""
for i in range(1,row+1):
    if((i<=3)or(i>=7 and i<=9)or(i>=13 and i<=15)):
        for j in range(1,col):
            result_str=result_str+"o"
        result_str=result_str+"\n"
    elif(i>=4 and i<=6):
        for j in range(1,5):
            result_str=result_str+"o"
        result_str=result_str+"\n"
    else:
        for j in range(1,14):
            result_str=result_str+" "
        for j in range(1,5):
            result_str=result_str+"o"
        result_str=result_str+"\n"
print(result_str);
