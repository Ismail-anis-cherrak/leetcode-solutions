class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: 
            return 0
        
        j=0
        
        for e in nums:
            if e != val:
                nums[j] = e
                j+=1
        return j
    

s = Solution()
print(s.removeElement([3,3,1,3,3], 3))
