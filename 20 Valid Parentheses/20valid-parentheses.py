class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dictionary = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary:
                if not stack or stack.pop() != dictionary[char]:
                    return False
            else:
                # Ignoring other characters
                continue

        # If stack is empty, all brackets were closed properly
        return not stack