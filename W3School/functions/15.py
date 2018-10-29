def sortstring(str):

    str = input("Please enter the string : ")

    data = [n for n in str.split("-")]

    data.sort()

    print('-'.join(data))

print(sortstring(str))
