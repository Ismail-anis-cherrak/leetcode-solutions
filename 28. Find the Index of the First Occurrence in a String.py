class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, h = len(needle), len(haystack)
        if n > h:
            return -1
        
        #! easy method:
        # for i in range(h - n + 1):
        #     if haystack[i:i+n] == needle:
        #         return i
        
        
        #! old method (comparing character by character): 
        for i in range(h - n + 1):
            match = True
            for j in range(n): 
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i

        return -1

s = Solution()
print(s.strStr("hello", "ll"))  # 2
print(s.strStr("hello", "hello"))  # 0
print(s.strStr("hello", "dummy"))  # 0
