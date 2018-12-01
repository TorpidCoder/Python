class School:

    def input(self):
        self.rollno = int(input("Please enter the roll number : "))
        self.name = input("Please enter the name : ")
        self.marks1 = int(input("Please enter the marks in 1 subject"))
        self.marks2 = int(input("Please enter the marks in 2 subject"))
        self.marks3 = int(input("Please enter the marks in 3 subject"))
        self.marks4 = int(input("Please enter the marks in 4 subject"))
        self.marks5 = int(input("Please enter the marks in 5 subject"))

    def calc(self):
        self.total = self.marks1+self.marks2+self.marks3+self.marks4+self.marks5
        self.average = self.total/5
        if(self.average>75):
            print("A")
        elif(self.average>60 and self.average<74):
            print("B")
        elif(self.average>40 and self.average<59):
            print("C")
        else:
            print("Fail")

    def display(self):
        print("The roll number is : ",self.rollno)
        print("The name is : ",self.name)
        print("The total marks is : " , self.total)
        print("The average marks is : ", self.average)

    def getRollNumber(self):
        return self.rollno

arr = []

studentlimit = int(input("Please enter the number of students : "))

for vals in range(0,studentlimit):
    obj = School()
    obj.input()
    obj.calc()
    arr.append(obj)

rollnumberfind = int(input("Roll number : "))

for vals in arr:
    if vals.getRollNumber()==rollnumberfind:
        vals.display()
