class Solution:
    def isValid(self, s: str) -> bool:

        key = {")":"(", "}":"{", "]":"["}

        cdStack = []

        for p in s:
            if p in key:
                if cdStack and cdStack[-1] == key[p]:
                    cdStack.pop()
                else:
                    return False
            
            else:
                cdStack.append(p)
        
        return True if not cdStack else False

        