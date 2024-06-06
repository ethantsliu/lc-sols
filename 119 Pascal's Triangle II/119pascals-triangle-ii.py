class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        current, previous = ([] for i in range(2))
        if rowIndex == 0: return [1]

        elif rowIndex == 1: return [1, 1]

        previous = [1, 1]

        for i in range(1, rowIndex): 
            current = []
            current.append(1)
            for j in range(len(previous)-1):
                current.append(previous[j] + previous[j+1])
            current.append(1)

            previous = current
        
        return current




        