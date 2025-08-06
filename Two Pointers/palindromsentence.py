import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        proc_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        i = 0
        j = len(proc_string) - 1
        
        while(i<j):
            if(proc_string[i] != proc_string[j]):
                return False

            i += 1
            j -= 1
        
        return True
        
    
sol = Solution()
vl = sol.isPalindrome('race a car')
print(vl)