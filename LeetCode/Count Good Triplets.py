from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if (abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c):
                        answer += 1
        return answer

sol = Solution()
print(sol.countGoodTriplets([3,0,1,1,9,7],7,2,3))