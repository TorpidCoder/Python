class student:

    def input(self):

        print(self)

        rollno = int(input("Enter the roll number  : "))
        name = input("Enter the name  : ")
        marks1 = int(input("Enter the marks1  : "))
        marks2 = int(input("Enter the marks2  : "))
        marks3 = int(input("Enter the marks3  : "))
        marks4 = int(input("Enter the marks4  : "))
        marks5 = int(input("Enter the marks5  : "))


    def calculate(self2):

        print(self2)

        total = self.marks1+self.marks2+self.marks3+self.marks4+self.marks5

        average = total/5

    def display(self):

        print(self)

        print("The total is : " , self.total)

        print("The average is : " , self.average)


obj = student()

obj.input()
obj.calculate()
obj.display()
