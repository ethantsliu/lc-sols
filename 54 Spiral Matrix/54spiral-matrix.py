class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        while matrix:
            res.extend(matrix.pop(0))

            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop(-1))

            if matrix: 
                res.extend(matrix.pop(-1)[::-1])

            if matrix and matrix[0]:
                for i in range(len(matrix)-1, -1, -1):
                    res.append(matrix[i].pop(0))
            
        return res
        