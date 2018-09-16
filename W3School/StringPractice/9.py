def remove(string,n):

    first_letter = string[:n]
    last_letter = string[n+1:]

    return first_letter+last_letter


print(remove("Python",3))
