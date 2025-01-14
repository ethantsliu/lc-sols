class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0

        for i in range(len(points)-1):
            time += max(abs(points[i+1][0] - points[i][0]), 
                        abs(points[i+1][1] - points[i][1]))

        return time