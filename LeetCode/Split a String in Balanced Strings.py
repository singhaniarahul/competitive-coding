class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        status = 0
        for i in range(0,len(s)):
            if s[i] == 'R':
                status += 1
            else:
                status -= 1
            if(status == 0):
                count += 1
        return count

sol = Solution()
print(sol.balancedStringSplit('RLRRRLLRLL'))