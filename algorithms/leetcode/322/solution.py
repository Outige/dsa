from collections import defaultdict

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Edge: Amount = 0
        if amount == 0:
            return 0

        coinHash = defaultdict(bool)
        for coin in coins:
            coinHash[coin] = True

        dp = [None] * (amount+1)
        for i in range(len(dp)):
            if coinHash[i]:
                dp[i] = 1
                continue
            options = []
            for coin in coins:
                if i-coin > 0 and dp[i-coin] != None:
                    options.append(dp[i-coin] + 1)
            if len(options) > 0:
                dp[i] = min(options)
        
        if dp[-1] == None:
            return -1
        return dp[-1]
