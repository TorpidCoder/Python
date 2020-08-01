__author__ = "ResearchInMotion"

def uniqueCharacter(word):

    freq = {}
    for i in word:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] +=1

    for i in range(len(word)):
        if freq[word[i]] == 1 :
            return i
    return -1

print(uniqueCharacter("alphabet"))
print(uniqueCharacter("barbados"))
