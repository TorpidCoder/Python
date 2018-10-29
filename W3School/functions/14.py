import string
def pangram(str,alphabet = string.ascii_lowercase):

    alpha_set = set(alphabet)

    return alpha_set <= set(str.lower())

print(pangram("The quick brown fox jumps over the lazy dog"))
