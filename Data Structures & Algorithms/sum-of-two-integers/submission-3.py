class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b & mask:
            carry = (a & b) << 1
            a ^= b 
            b = carry
            
        return (a & mask) if b > mask else a

        # return a