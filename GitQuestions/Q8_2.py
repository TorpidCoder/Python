alpha = input("Enter the words : ")

items = [x for x in alpha.split(',')]

print(sorted(list(set(items))))
