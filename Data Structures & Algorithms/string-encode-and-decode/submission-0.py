class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            strLen = len(s)
            encoded += f"{strLen}#{s}"
        
        return encoded


    def decode(self, s: str) -> List[str]:
        
        ans = []
        char = 0
        
        while char < len(s):
            charEND = char
            while s[charEND] != '#':
                charEND += 1
            length = int(s[char:charEND])
            char = charEND + 1
            charEND = char + length
            ans.append(s[char:charEND])
            char = charEND
        
        return ans



