class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        i = 0
        for j in range(0, len(nums) -1):
            if nums[j] != nums [j+1]:
                i+=1
                nums[i] = nums[j+1]

        return i + 1


s = Solution()
nums = [1, 2]
print(s.removeDuplicates(nums))
print(nums)