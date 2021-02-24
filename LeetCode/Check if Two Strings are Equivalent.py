from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_string = ''
        second_string = ''
        for i in range(0, len(word1)):
            first_string += word1[i]
        for i in range(0, len(word2)):
            second_string += word2[i]
        if first_string == second_string:
            return True
        return False

sol = Solution()
print(sol.arrayStringsAreEqual(["abc", "d", "defg"],['abcddefg']))