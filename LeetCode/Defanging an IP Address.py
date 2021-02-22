class Solution:
    def defangIPaddr(self, address: str) -> str:
        defangedIP = ''
        for i in range(0,len(address)):
            #print(i)
            if(address[i]=='.'):
                defangedIP += '[.]'
            else:
                defangedIP += address[i]
        return defangedIP

sol = Solution()
print(sol.defangIPaddr('255.100.50.0'))