import math

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {value: index for index, value in enumerate(nums)}
        index = -1
        for oneindex in range(len(nums) - 1):
            val = target - nums[oneindex]
            index = num_dict.get(val, float('nan'))

            if(not math.isnan(index) and oneindex != index):
                break

        return [oneindex, index]


sol = Solution()
val = sol.twoSum([2, 5, 5, 11], 10)
print(val)

            