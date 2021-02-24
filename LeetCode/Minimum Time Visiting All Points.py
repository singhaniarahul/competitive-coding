from typing import List
import math

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0
        currentPoint = points[0]
        for i in range(1, len(points)):
            targetPoint = points[i]
            totalTime += abs(targetPoint[1]-currentPoint[1]) if abs(targetPoint[1]-currentPoint[1]) > abs(targetPoint[0]-currentPoint[0]) else abs(targetPoint[0]-currentPoint[0])
            currentPoint = targetPoint
        return totalTime

sol = Solution()
print(sol.minTimeToVisitAllPoints([[3,2],[-2,2]]))