list = [1,2,3,4,5,6,7,8,9,10]

position = 3-1
index = 0
leng = len(list)

while leng>0:
    index = (position+index)%leng
    print(list.pop(index))
    leng-=1



print(list)
