__author__ = "ResearchInMotion"

num1 = input("Please enter the number 1 : ")
num2 = input("Please enter the number 2 : ")
# num1 = [int(number) for number in num1]
# num2 = [int(number) for number in num2]
# sum1 = 0
# sum2 = 0
# for values in num1:
#     sum1 += values
# print("The sum of first number :" , sum1)
#
# for values in num2:
#     sum2 += values
# print("The sum of first number :" , sum2)

num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
print(sum)


def solution(num1, num2):
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))


print(solution(num1, num2))