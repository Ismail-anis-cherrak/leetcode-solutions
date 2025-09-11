class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits
    

s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([1,2,9]))
print(s.plusOne([1,2,9,9]))
print(s.plusOne([1,9,9,9]))
print(s.plusOne([9,9,9]))