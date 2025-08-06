from collections import Counter
import numbers

def is_number(n):
    return isinstance(n, numbers.Number) and not isinstance(n, bool)


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i = 1
        j = 1

        while j < n:
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
            
            j += 1
        return i
    
sol = Solution()
val = sol.removeDuplicates([1])
print(val)