marks_1 = int(input("Enter the marks in subject 1 : "))

marks_2 = int(input("Enter the marks in subject 2 : "))

marks_3 = int(input("Enter the marks in subject 3 : "))

marks_4 = int(input("Enter the marks in subject 4 : "))

marks_5 = int(input("Enter the marks in subject 5 : "))

total = marks_1+marks_2+marks_3+marks_4+marks_5

percentage = total/5

if(percentage>90):
    print("S")
elif(percentage>76) & (percentage<90):
    print("A")
elif(percentage>61) & (percentage<75):
    print("B")
elif(percentage>51) & (percentage<60):
    print("C")
elif(percentage>40) & (percentage<50):
    print("D")
else:
    print("Fail")
