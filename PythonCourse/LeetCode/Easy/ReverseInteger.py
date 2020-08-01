__author__ = "ResearchInMotion"

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21

number = input("Please enter the number : ")
number = [values for values in str(number)]
if '-' in number:
    newnumber = int('-' + "".join(number[:0:-1]))
else:
    newnumber = int("".join(number[::-1]))
print(newnumber)