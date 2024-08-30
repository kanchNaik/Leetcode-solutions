class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        i = m -1
        j = n -1
        k = m + n -1

        while(j >= 0 and i >= 0):
            if(nums2[j] > nums1[i]):
                nums1[k] = nums2[j]
                j -= 1
            elif(nums2[j] == nums1[i]):
                nums1[k] = nums2[j]
                k -= 1
                nums1[k] = nums1[i]
                j -= 1
                i -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        while(j >= 0):
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        print(nums1)

sol = Solution()
sol.merge([1, 2, 3, 4, 0, 0, 0], 4, [6, 8, 9], 3)