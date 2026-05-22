class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ("(", "{", "["):
                stack.append(i)
            if i in (")","}","]"):
                if len(stack) == 0:
                    return False
                b = stack.pop()
                if i == ")" and b != "(":
                    return False
                if i == "}" and b != "{":
                    return False
                if i == "]" and b != "[":
                    return False
        
        if len(stack) != 0:
            return False
        
        return True

