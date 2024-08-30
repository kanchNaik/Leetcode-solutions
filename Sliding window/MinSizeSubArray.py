class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = j = sum =0
        # len_nums = len(nums)
        # minlen = len_nums + 1

        # while(j < len_nums):

        #     sum += nums[j]
        #     if(sum >= target):
        #         minlen = min(minlen, j - i + 1)

        #     while(sum > target and i < j):
        #         sum -= nums[i]
        #         i += 1
        #         if(sum >= target):
        #             minlen = min(minlen, j - i + 1)

        #     j += 1
        # return 0 if (minlen == len_nums + 1) else minlen

        sortednums = sorted(nums)
        while(j < len(nums) and sum < target):
            sum += nums[j]
            j += 1
        return j if sum >= target else 0
    


sol = Solution()
val = sol.minSubArrayLen(4, [1,4,4])
print(val)
