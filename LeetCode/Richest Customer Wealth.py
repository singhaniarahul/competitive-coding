class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(0, len(accounts)):
            currentWealth = 0
            for j in range(0, len(accounts[i])):
                currentWealth += accounts[i][j]
            maxWealth = currentWealth if currentWealth > maxWealth else maxWealth
        return maxWealth