class InputOutString:

    def getString(self):
        self.string = input("Please enter the string :")


    def printString(self):
        self.upper = self.string.upper()
        print(self.upper)



obj = InputOutString()
obj.getString()
obj.printString()
