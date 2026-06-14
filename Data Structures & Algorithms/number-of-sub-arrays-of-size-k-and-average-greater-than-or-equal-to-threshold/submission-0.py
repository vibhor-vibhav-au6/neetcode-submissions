class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        def average(arr, k):
            s = 0
            for i in arr:
                s += i
            
            return s/k
        
        res = 0
        
        for l in range(len(arr) - k + 1):
            avg = average(arr[l:l+k], k)
            if avg >= threshold:
                res += 1

        
        return res


