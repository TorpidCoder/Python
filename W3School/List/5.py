list = ['abc', 'xyz', 'aba', '1221']

count = 0

for vals in list:
    if(len(vals)>2):
        if(vals[-1]==vals[:1]):
            count+=1


print(count)
