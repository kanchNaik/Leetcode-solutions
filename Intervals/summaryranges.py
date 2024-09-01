class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        m = len(nums)

        if(m == 0):
            return []
            
        ranges = []
        summary = []
        i = 0
        j = 1
        
        pre = nums[i]
        post = nums[i]

        while(j < m):
            if(nums[j] == post + 1):
                post = nums[j]
            else:
                summary.append([pre, post]) 
                pre = nums[j]
                post = nums[j]  

            j += 1

        summary.append([pre, post])

        for item in summary:
            if(item[0] == item[1]):
                ranges.append(f"{item[0]}")
            else:
                ranges.append(f"{item[0]}->{item[1]}")
        
        return ranges

sol = Solution()
sol.summaryRanges([0,2,3,4,6,8,9])
        

