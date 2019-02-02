
def maximumSum(list1):
    maxi = 0
    for x in Sample_lists:
        sum=0
        for y in x:
            sum+=y
        maxi = max(sum,maxi)
    return maxi

Sample_lists= [1,2,3], [4,5,6], [10,11,12], [7,8,9]


print(maximumSum(Sample_lists))


print(max(Sample_lists, key=sum))
