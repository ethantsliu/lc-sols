class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        length = len(string)//2
        for i in range(length):
            if (string[i] != string[-1-i]):
                return False
        return True