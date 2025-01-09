class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i.isalnum():
                stack.append(i.lower())
        
        for i in range(len(stack)//2):
            if stack[i] != stack[len(stack)-i-1]: return False

        return True