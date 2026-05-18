class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = word1[0]
        p2 = word2[0]

        res = ""

        l = min(len(word1), len(word2))

        for i in range(l):
            res += word1[i]
            res += word2[i]

        res += word1[l:]
        res += word2[l:]

        return res