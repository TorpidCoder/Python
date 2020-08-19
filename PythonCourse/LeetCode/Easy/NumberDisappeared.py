__author__ = "ResearchInMotion"

arr = [4,3,2,7,8,2,3,1]
def find_missing(lst):
    sortedarr = sorted(lst)
    vals = sorted(set(range(sortedarr[0], sortedarr[-1])) - set(sortedarr))
    return vals

print(find_missing(arr))