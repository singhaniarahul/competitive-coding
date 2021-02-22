from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in range(0,len(stones)):
            count += jewels.count(stones[i])
        return count

sol = Solution()
print(sol.numJewelsInStones('aA','aAAbbbb'))