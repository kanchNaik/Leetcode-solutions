class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ransomNote = {}
        dict_magazine = {}
        isvalid = True

        if(len(ransomNote) > len(magazine)):
            return not isvalid

        for c in magazine:
            if c in dict_magazine:
                dict_magazine[c] += 1
            else:
                dict_magazine[c] = 1

        
        for c in ransomNote:
            if c in dict_magazine and dict_magazine[c] > 0:
                dict_magazine[c] -= 1
            else:
                isvalid = False
                break

        return isvalid
    
sol = Solution()
isval = sol.canConstruct('fihjjjei', 'hjibagacbhadfaefdjaeaebgi')
print(isval)