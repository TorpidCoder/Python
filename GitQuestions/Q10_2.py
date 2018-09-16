
words = input("Please enter the words : ")

items = [x for x in words.split(' ')]

print(" ".join((sorted(list(set(items))))))
