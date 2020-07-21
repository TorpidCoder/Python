__author__ = "ResearchInMotion"

# Kids With the Greatest Number of Candies
#
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
# Explanation:
# Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids.
# Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.
# Kid 3 has 5 candies and this is already the greatest number of candies among the kids.
# Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies.
# Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.


candies = [4,2,1,1,2]
extraCandies = 1


# Calculate the max here
max = candies[0]
for values in candies:
    if(values > max):
        max = values


newCandies = [extraCandies + vals for vals in candies]
print(newCandies)
answer = [vals >=max for vals in newCandies]
print(answer)



