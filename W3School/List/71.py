def dictionaryEmpty(arr):
    if(all(not vals for vals in arr)):
        return True
    else:
        return False


arr = [{},{},{}]
print(dictionaryEmpty(arr))
