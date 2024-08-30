class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        m = len(nums)
        if(m <= 2):
            print(m)
        
        j =2

        for i in range(2, m):
            if(nums[i] != nums[j -2]):
                nums[j] = nums[i]
                j +=1
            i += 1
        
        for k in range(j, m):
            nums[k] = '_'
        
        print(f'{j} - nums {nums}')

sol = Solution()
sol.removeDuplicates([0, 1])