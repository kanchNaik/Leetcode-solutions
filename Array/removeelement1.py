from typing import List, Union

def countIntegerElements(nums) -> int:
        count = 0
        for num in nums:
            if isinstance(num, int):
                count += 1
        return count

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        j = 0
        i = 0

        while(j < len(nums)): 

            if(nums[j] == val):
                 nums[j] = '_'
                 i = j
            else:     
                while(k < len(nums) and nums[k] != '_'):
                     k += 1

                if(k >= len(nums)):
                    k = i

                if(nums[k] == '_'):
                    nums[k] = nums[j]
                    nums[j] = '_' 
                
            j += 1

        count = countIntegerElements(nums)
        print(nums)
        return count
    
sol = Solution()
val = sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(val)