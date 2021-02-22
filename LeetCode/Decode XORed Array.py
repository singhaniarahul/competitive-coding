from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = []
        answer.append(first)
        answer.append(first ^ encoded[0])
        for i in range(1,len(encoded)):
            answer.append(encoded[i]^answer[i])
        return answer

sol = Solution()
print(sol.decode([1,2,3],1))