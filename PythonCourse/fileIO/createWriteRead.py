__author__ = "ResearchInMotion"


# file create and write
with open(file="/Users/sahilnagpal/PycharmProjects/Python/PythonCourse/fileIO/MyFile.txt" , mode='w+' , encoding='utf=8') as file:
    file.write("My Name is Sahil")
    file.write("\n")
    file.write("My Name is Nikki")
    file.write("\n")
    file.write("Whoever said i dont give a fuck")

with open(file="/Users/sahilnagpal/PycharmProjects/Python/PythonCourse/fileIO/MyFile.txt" , mode='r' , encoding='utf=8') as fileread:
    data = fileread.read().splitlines()
    for values in data:
        print(values)

