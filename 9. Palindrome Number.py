class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        #! First method : 
        #? return str(x) == str(x)[::-1]
        #! Second method :
        for i in range (len(str(x)) // 2):
            if str(x)[i] != str(x)[len(str(x)) - 1 - i]:
                return False
        return True


s = Solution()
print(s.isPalindrome(121))  # True
print(s.isPalindrome(-121)) # False
print(s.isPalindrome(10))   # False
print(s.isPalindrome(-101)) # False
print(s.isPalindrome(0))    # True

