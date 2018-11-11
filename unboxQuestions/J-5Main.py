class student:

    def __init__(self):

        self.rollno = 0
        self.name = ''
        self.address = ''
        self.city = ''

    def input(self):

        self.rollno = int(input("Please enter the roll number : "))
        self.name = input("Please enter the name : ")
        self.address = input("Please enter the address : ")
        self.city = input("Please enter the city : ")

    def display(self):
        print("The roll number is : ",self.rollno)
        print("The name is :" , self.name)
        print("The address is :",self.address)
        print("The city is :",self.city)

    def getRollNumber(self):
        return self.rollno


arr = []

strengthofclass = int(input("Number of students is : "))

for vals in range(0,strengthofclass):
    obj = student()
    obj.input()
    arr.append(obj)

rollnumbersearch = int(input("Roll number to search : "))

for vals in arr:
    if vals.getRollNumber() == rollnumbersearch:
        vals.display()
