class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if(n< m) :
            return -1
        
        i = 0
        while(i < n):
            if(haystack[i: i + m] == needle):
                return i
            
            i += 1

sol = Solution()
val = sol.strStr('Mississippi', 'issip')
print(val)