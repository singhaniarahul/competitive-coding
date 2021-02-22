class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        product = 1
        while(temp>0):
            product *= temp%10
            temp //= 10
        temp = n
        sum = 0
        while(temp>0):
            sum += temp%10
            temp //= 10
        return product-sum

sol = Solution()
print(sol.subtractProductAndSum(234))
