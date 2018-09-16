def longest(word_list):
    word_len = []

    for vals in word_list:
        word_len.append((len(vals),vals))
    word_len.sort()
    print(word_len)
    return word_len[-1][1]



print(longest(["sahil" , "nik"]))
