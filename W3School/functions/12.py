def palindrome(str):

    rev = str[::-1]
    if(rev == str):
        print("String is palindrome")
    else:
        print("not a palindrome")

print(palindrome("nitin"))
