class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        dict_majorityElement = {}

        for n in nums:
            if(n in dict_majorityElement):
                dict_majorityElement[n] += 1
            else:
                dict_majorityElement[n] = 1

        majority_element = max(dict_majorityElement, key=dict_majorityElement.get)
        print(majority_element)

sol = Solution()
val = sol.majorityElement([2, 2, 1, 1, 1, 2, 2, 3, 3])


## Optimized 
from collections import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = 0
        r = 0

        for num in nums:
            if(m == 0):
                r = num
            
            if(num == r):
                m += 1
            else:
                m -= 1
        
        return r