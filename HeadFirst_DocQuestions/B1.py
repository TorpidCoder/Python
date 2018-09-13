name = input("Please enter your name : ")

marks_1 = int(input("Enter the marks in subject 1 : "))

marks_2 = int(input("Enter the marks in subject 2 : "))

marks_3 = int(input("Enter the marks in subject 3 : "))

marks_4 = int(input("Enter the marks in subject 4 : "))

marks_5 = int(input("Enter the marks in subject 5 : "))

total = marks_1+marks_2+marks_3+marks_4+marks_5

percentage = total/5

print("The total is {} ".format(total))

print("The percentage is {} ".format(percentage))

if(percentage>40):
    print("You are pass")
else:
    print("You are fail")
