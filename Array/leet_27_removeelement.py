from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for placing non-val elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Overwrite val occurrences
                k += 1  # Move the pointer forward
        
        return k