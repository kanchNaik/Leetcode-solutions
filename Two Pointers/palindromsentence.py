import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # proc_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # print(proc_string)
        # i = 0
        # j = len(proc_string) - 1
        # isvalid = True

        # while(i<j):
        #     if(proc_string[i] != proc_string[j]):
        #         isvalid = False
        #         break;

        #     i += 1
        #     j -= 1

        isvalid = True
        s = s.lower()
        i = 0
        j = len(s) - 1

        while(i<j):
            print(f'i = {s[i]} - j = {s[j]}')
            if(not s[i].isalnum()):
                i += 1
            elif(not s[j].isalnum()):
                j -= 1
            elif(s[i] == s[j]):
                i += 1
                j -= 1
            else:
                isvalid = False
                break
        

        return isvalid
    
sol = Solution()
vl = sol.isPalindrome('race a car')
print(vl)