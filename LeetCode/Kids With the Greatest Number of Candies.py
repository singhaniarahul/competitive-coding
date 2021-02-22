from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        for i in range(0,len(candies)):
            maxCandies = candies[i] if candies[i] > maxCandies else maxCandies
        answer = []
        for i in range(0,len(candies)):
            if(candies[i]+extraCandies >= maxCandies):
                answer.append(True)
            else:
                answer.append(False)
        return answer

sol = Solution()
print(sol.kidsWithCandies([12,1,12],10))