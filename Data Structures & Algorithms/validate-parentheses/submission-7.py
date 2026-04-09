class Solution:
    def isValid(self, s: str) -> bool:

        mapCLAW = {")": "(", "]": "[", "}": "{"}
        
        stack = []
        
        for char in s:
            if char not in mapCLAW:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != mapCLAW[char]:
                    return False
                stack.pop()
        
        if len(stack) > 0:
            return False
        return True

        