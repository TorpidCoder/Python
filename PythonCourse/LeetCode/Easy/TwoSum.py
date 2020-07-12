__author__ = "ResearchInMotion"


#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(mylist , target):
    if len(mylist) <1:
        return "List is not Appropriate"

    dictvalues = {}
    for i in range(len(mylist)):
        if mylist[i] in dictvalues:
            return [dictvalues[mylist[i]] , i]
        else:
            dictvalues[target - mylist[i]] = i

print(twoSum(mylist=[1,2,3,4,5,6,7] , target=6))


