def check(string , sub):
    if (string.find(sub) == -1):
        return "no"
    else:
        return "yes"

string = input("Please enter the string 1 : ")

sub = input("Please enter the string 2 : ")

print(check(string , sub))
