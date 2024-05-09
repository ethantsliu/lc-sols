class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        check = []
        nums = []
        for i in range(len(s)):
            if s[i] in check: 
                nums.append(len(check))
                del check[:check.index(s[i])+1]
            check.append(s[i])
        nums.append(len(check))
    
        return max(nums)
