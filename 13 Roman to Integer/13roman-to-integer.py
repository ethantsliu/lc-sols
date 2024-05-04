class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = 0
        for char in s:
            current = roman_map[char]
            if current > prev: 
                sum += current-2*prev
            else: sum += current
            prev = current
        return sum