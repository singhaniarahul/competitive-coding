from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffledArray = []
        for i in range(0,n):
            shuffledArray.append(nums[i])
            shuffledArray.append(nums[i+n])
        return shuffledArray

sol = Solution()
print(sol.shuffle([2,5,1,3,4,7],3))