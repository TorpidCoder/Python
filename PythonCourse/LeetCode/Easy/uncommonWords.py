class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1
        print(count)

        return [word for word in count if count[word] == 1]

S = Solution()
print(S.uncommonFromSentences("this apple is sweet" , "this apple is sour"))