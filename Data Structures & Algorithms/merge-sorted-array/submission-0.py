class Solution:
    def merge(self, n1: List[int], m: int, n2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p2 >= 0:
            if p1 >= 0 and n1[p1] >= n2[p2]:
                n1[last] = n1[p1]
                
                p1 -= 1
            else:
                n1[last] = n2[p2]
                p2 -= 1
            
            last -= 1
        