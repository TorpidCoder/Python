list = []

sent1 = input("Sentence  : ")

sent2 = input("Sentence  : ")

list.append(sent1)
list.append(sent2)

print(list)


swap = sent1,sent2=sent2,sent1

list.append(swap)

print(list)
