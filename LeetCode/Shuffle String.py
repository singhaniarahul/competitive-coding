from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = []
        for i in range(0, len(indices)):
            result.append('')
        for i in range(0, len(indices)):
            result[indices[i]] = s[i]
        resultStr = ''
        for i in range(0, len(result)):
            resultStr = resultStr + result[i]
        return resultStr

sol = Solution()
print(sol.restoreString('codeleet',[4,5,6,7,0,2,1,3]))