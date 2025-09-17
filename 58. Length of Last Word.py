class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1
        
        while i >= 0 and s[i] == ' ':
            i-=1
        
        while i >= 0 and s[i] != ' ':
            length +=1 
            i-=1
        
        return(length)





s = Solution()
print(s.lengthOfLastWord(""))
print(s.lengthOfLastWord("Hello World"))           # Output: 5
print(s.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(s.lengthOfLastWord("luffy is still joyboy")) # Output: 6