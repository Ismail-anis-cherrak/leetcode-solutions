class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: 
            return 0 
        if nums[0] >= target:
            return 0
        for i,e in enumerate(nums):
            if e == target:
                return i  
            elif e > target and nums[i-1] < target:
                return i 
        return len(nums)
    
s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))