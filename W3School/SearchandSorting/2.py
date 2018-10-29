def linear(arr,num):

    for vals in range(0,len(arr)):
        if(arr[vals]==num):
            return True
        else:
            return -1


arr = [11,23,58,31,56,77,43,12,65,19]
num = 11

result= linear(arr,num)

if(result!=-1):
    print(True)
else:
    print(False)
