class Solution:
    def relativeSortArray(self, arr1, arr2):
        d1 = {}
        for i in arr2:
            d1[i] = 1
        not_match = []
        d2 = {}
        for i in arr1:
            if i in d1:
                d2[i] = d2.setdefault(i,0) + 1
            else:
                not_match.append(i)
        match = []
        for i in arr2:
            match += [i] * d2[i]
        return match + sorted(not_match)