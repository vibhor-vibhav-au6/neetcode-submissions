class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        if len(s) != len(t): return False
        for i in s:
            if i in seen_s:
                seen_s[i] += 1
            else:
                seen_s[i] = 1

        for i in t:
            if i in seen_t:
                seen_t[i] += 1
            else:
                seen_t[i] = 1

        for k,v in seen_s.items():
            if k not in seen_t:
                return False
            if v != seen_t[k]:
                return False
        
        return True
            