class Student:

    def input(self):
        self.rollno = int(input("enter the roll number : "))
        self.name = input("enter the name : ")
        self.subject1 = int(input("enter the number : "))
        self.subject2 = int(input("enter the number : "))
        self.subject3 = int(input("enter the number : "))
        self.subject4 = int(input("enter the number : "))
        self.subject5 = int(input("enter the number : "))

    def calculate(self):
        self.total = self.subject1+self.subject2+self.subject3+self.subject4+self.subject5
        self.average =self.total/5

    def display(self):
        print("The name is : " ,self.name)
        print("The roll number is : ", self.rollno)
        print("The total is : ", self.total)
        print("The average is : ", self.average)

o1 = Student()

o1.input()
o1.calculate()
o1.display()
