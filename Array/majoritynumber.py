
#This code is suitable if we assume majority element will be present more than n/2 times 
#Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        m = 0
        r = 0

        for num in nums:
            if(m == 0):
                r = num
            
            if(num == r):
                m += 1
            else:
                m -= 1

        print(r)

sol = Solution()
sol.majorityElement([2, 2, 1, 1, 1, 2, 2])
