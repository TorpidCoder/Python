__author__ = "ResearchInMotion"

string = input("Enter the word : ")
if(string == string[::-1]):
    print("Palindrome")
else:
    print("Not a Palindrome")
