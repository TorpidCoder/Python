__author__ = "ResearchInMotion"

# creating a file
with open(file="/Users/sahilnagpal/PycharmProjects/Python/PythonCourse/CustomException/File.txt" , mode='w' , encoding='utf-8') as file:
    file.write("My Name is Sahil. This is my file exception tutorial")
    file.close()
print("File created")

# reading the file in try block

try:
    open(file="/Users/sahilnagpal/PycharmProjects/Python/PythonCourse/CustomException/File2.txt" , mode='r')
    print("File Present")
except FileNotFoundError as ex:
    print("File not found ")
    print(ex.args)

