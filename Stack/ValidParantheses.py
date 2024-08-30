class Solution:
    def isValid(self, s: str) -> bool:
        openingbracketStack = list()
        valid = True
        openclosebrack = {'(' : ')', '{': '}', '[': ']'}
        
        for char in s:
            if(char in ['(', '[', '{']):
                openingbracketStack.append(char)
            elif(len(openingbracketStack) > 0 and openclosebrack[openingbracketStack[-1]] == char):
                del openingbracketStack[-1]
            else:
                valid = False

        if(len(openingbracketStack) != 0):
            valid = False

        return valid
    
sol = Solution()
valid = sol.isValid('[')
print(valid)