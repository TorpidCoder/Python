marks_1 = int(input("Enter the marks in subject 1 : "))

marks_2 = int(input("Enter the marks in subject 2 : "))

marks_3 = int(input("Enter the marks in subject 3 : "))

marks_4 = int(input("Enter the marks in subject 4 : "))

marks_5 = int(input("Enter the marks in subject 5 : "))

total = marks_1+marks_2+marks_3+marks_4+marks_5

percentage = total/5


print("The percentage is {}  and the total is {}".format(percentage,total))

if(percentage>60):
    print("First")
elif(percentage>50) & (percentage<59):
    print("Second")
elif(percentage>40) & (percentage<49):
    print("Third")
else:
    print("Fail")
