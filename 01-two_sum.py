class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevHashMap = {}
        for i, e in enumerate(nums):
            diff = target - e
            if diff in prevHashMap:
                return [prevHashMap[diff], i]
            prevHashMap[e] = i
        return []
    

#testing the solution
s=Solution()
print(s.twoSum([2,4,5,2,19],7))