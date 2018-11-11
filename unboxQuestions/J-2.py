class Emp:

    def input(self):
        self.Ecode=int(input("Please enter the Employee Code "))
        self.Ename=input("Please enter your Name ")
        self.BasicSalary=int(input("Please enter your basic salary "))

    def calc(s):
        s.HRA=0.40*s.BasicSalary
        s.DA=0.20*s.BasicSalary
        s.TA=0.10*s.BasicSalary
        s.GrossSalary=s.BasicSalary+s.HRA+s.DA+s.TA
        s.IT=0.20*s.GrossSalary
        s.PF=0.10*s.GrossSalary
        s.NetSalary=s.GrossSalary-(s.IT+s.PF)


    def disp(this):
        print("The employee code is ",this.Ecode)
        print("The name of empolyee is ",this.Ename)
        print("The basic salary is ",this.BasicSalary)
        print("The HRA is ",this.HRA)
        print("The DA is ", this.DA)
        print("The TA is ", this.TA)
        print("The Gross Salary is ", this.GrossSalary)
        print("The IT is ", this.IT)
        print("The PF is ", this.PF)
        print("The Net Salary is ", this.NetSalary)

    def getCode(self):
        return self.Ecode

arr = []

numberofemployees = int(input("Please enter the number of employees : "))

for vals in range(0,numberofemployees):
    obj = Emp()
    obj.input()
    obj.calc()
    arr.append(obj)

ecode_value =int(input("enter the ecode which you want to fetch : "))

for vals in arr:
    if(vals.getCode()==ecode_value):
        vals.disp() 
