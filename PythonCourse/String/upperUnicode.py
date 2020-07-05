__author__ = "ResearchInMotion"


message = input("Please enter the message  : ").upper()
for values in message:
    print(ord(values) ,end=" ")