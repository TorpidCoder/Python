class taxpayer:

    def input(self):
        self.pan = int(input("Enter the pan number : "))
        self.name = input("Enter the name : ")
        self.income = int(input("Enter the income : "))

    def calc(self):
        if(self.income<=100000):
            self.tax = self.income
        elif(self.income<100001 and self.income>200000):
            self.tax = self.income*0.10
        elif(self.income<200001 and self.income>500000):
            self.tax = self.income*0.15
        else:
            self.tax = self.income*0.20

    def display(self):
        print("The name is :" , self.name)
        print("The pan number is : " , self.pan)
        print("The income is : " , self.income)
        print("The tax is : " , self.tax)

    def getPan(self):
        return self.pan


arr = []

numberofemp = int(input("Please enter the employee count : "))

for vals in range(0,numberofemp):
    obj = taxpayer()
    obj.input()
    obj.calc()
    arr.append(obj)


pannumber= int(input("Please enter the pan number to fetch : "))

for vals in arr:
    if(vals.getPan()==pannumber):
        vals.display
    break
print("The id is not present")
