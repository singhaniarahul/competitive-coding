class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        currentDepth = 0
        for i in range(0,len(s)):
            if(s[i]=='('):
                currentDepth += 1
            elif(s[i]==')'):
                currentDepth -= 1
            answer = currentDepth if currentDepth > answer else answer
        return answer
            
sol = Solution()
print(sol.maxDepth('(1)+((2))+(((3)))'))