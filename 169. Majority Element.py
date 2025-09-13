class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map ={}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        return max(hash_map, key=hash_map.get)

s = Solution()
print(s.majorityElement([3,2,3,3,3,1,1,8,8,0]))          