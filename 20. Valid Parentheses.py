class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s: 
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack  # True if all brackets are matched and stack is empty
    

s = Solution()
print(s.isValid("()"))          # True
print(s.isValid("()[]{}"))      # True
print(s.isValid("(]"))          # False
print(s.isValid("([)]"))        # False
print(s.isValid("{[]}"))        # True
print(s.isValid(""))            # True
print(s.isValid("(("))          # False (here is the benefit of the not stack return )




