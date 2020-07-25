__author__ = "ResearchInMotion"

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# Current array : [1,1,4,2,1,3]
# Target array  : [1,1,1,2,3,4]

heights = [1,1,4,2,1,3]

newarr = sorted(heights)
print(len([index for index, (e1, e2) in enumerate(zip(heights, newarr)) if e1 != e2]))

