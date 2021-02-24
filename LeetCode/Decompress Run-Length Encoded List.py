from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressedList = []
        for i in range(0,len(nums),2):
            number = nums[i+1]
            for freq in range(nums[i],0,-1):
                decompressedList.append(number)
                freq -= 1
            i += 2
        return decompressedList

sol = Solution()
print(sol.decompressRLElist([1,2,3,4]))