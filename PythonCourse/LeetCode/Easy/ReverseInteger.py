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

number = int(input("Please enter the number : "))
number = str(number)
reversenumber = number[::-1]
reversenumber = int(reversenumber)
print(reversenumber)