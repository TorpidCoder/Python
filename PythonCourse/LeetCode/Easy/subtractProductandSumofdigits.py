__author__ = "ResearchInMotion"

def subtractProductAndSum(n):

    nums = [int(values) for values in str(n)]
    prod = 1
    sum = 0
    for vals in nums:
        prod *=vals
        sum += vals
    result = prod - sum
    return result

print(subtractProductAndSum(n=234))
