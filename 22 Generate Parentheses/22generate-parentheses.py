class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def helper(curr, open_count, close_count):
            if len(curr) == 2 * n:
                result.append(curr)
                return 

            if open_count < n:
                helper(curr + '(', open_count+1, close_count)
            
            if close_count < open_count:
                helper(curr + ')', open_count, close_count+1)

        result = []
        helper("", 0, 0)
        return result