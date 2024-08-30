from collections import Counter
import numbers

def is_number(n):
    return isinstance(n, numbers.Number) and not isinstance(n, bool)


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        i = 0
        j = i + 1
        k = 1
        numlen = len(nums)
        
        while(j < numlen):
            if(nums[i] == nums[j]):
                nums[j] = '_'
                j += 1 
            else:
                nums[k] = nums[j]
                if(k != j):
                    nums[j] = '_'

                i += 1
                j += 1
                k += 1
                
        
        return k
    
sol = Solution()
val = sol.removeDuplicates([1,1,2])
print(val)