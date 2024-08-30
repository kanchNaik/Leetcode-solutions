class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        n = x // 10
        rev = 0
        rem = x % 10

        while(rem != 0 or n != 0):
            rev = rev * 10 + rem
            rem = n % 10
            n = n // 10

        return True if (rev == x) else False
    
        

sol = Solution()
print(sol.isPalindrome(10))