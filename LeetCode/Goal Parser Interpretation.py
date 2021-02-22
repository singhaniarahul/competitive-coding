class Solution:
    def interpret(self, command: str) -> str:
        currentString = ''
        resultString = ''
        for i in range(0,len(command)):
            currentString += command[i]
            if(currentString=='G'):
                resultString += 'G'
                currentString = ''
            elif(currentString=='()'):
                resultString += 'o'
                currentString = ''
            elif(currentString=='(al)'):
                resultString += 'al'
                currentString = ''
        return resultString

sol = Solution()
print(sol.interpret('(al)G(al)()()G'))