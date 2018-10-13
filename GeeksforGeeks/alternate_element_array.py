def alternate(arr):

    arr2 =[]

    for count , vals in enumerate(arr):

        print(count,"-->" , vals)

        if(count%2!=0):

            arr2.append(vals)

    return arr2




arr = [1,1,3,78,5,23,71]

print(alternate(arr))
