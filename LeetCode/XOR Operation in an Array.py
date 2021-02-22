class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = 0
        for i in range(0,n):
            element = start + 2*i
            answer = answer ^ element
        return answer