class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in range(len(s)-1):
            if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                sum -= roman_numerals[s[i]]
            else:
                sum += roman_numerals[s[i]]
        return sum + roman_numerals[s[-1]]
    
s = Solution()
print(s.romanToInt("III"))      # 3
print(s.romanToInt("IV"))       # 4
print(s.romanToInt("IX"))       # 9
print(s.romanToInt("LVIII"))    # 58
print(s.romanToInt("MCMXCIV"))  # 1994
print(s.romanToInt("XL"))       # 40
print(s.romanToInt("XC"))       # 90
print(s.romanToInt("CD"))       # 400
print(s.romanToInt("CM"))       # 900
print(s.romanToInt("MMXXIV"))   # 2024
print(s.romanToInt("DCCCXC"))   # 890
print(s.romanToInt("LXXVII"))   # 77
print(s.romanToInt("XXI"))      # 21
print(s.romanToInt("I"))        # 1
print(s.romanToInt("MDCLXVI"))  # 1666