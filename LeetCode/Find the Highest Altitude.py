from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        currAlt = 0
        for i in range(0,len(gain)):
            currAlt += gain[i]
            maxAlt = currAlt if currAlt > maxAlt else maxAlt
        return maxAlt

sol = Solution()
print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))