class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counter = 0
        for i in reversed(range(len(s))):
            if counter != 0 and s[i] == " ": return counter
            if s[i] == " ": continue
            else: counter+=1 
        return counter