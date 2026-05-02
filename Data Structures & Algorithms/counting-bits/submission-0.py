class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for j in range (n + 1):
            i = j
            while i:
                if i & 1 == 1:
                    res[j] += 1
                
                i >>= 1
        
        return res

