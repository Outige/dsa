class Solution(object):
    def maxProfit(self, prices):
            """
            :type prices: List[int]
            :rtype: int
            """
            # Create a memory of the best possible purchase price at any given day
            l = 0
            r = len(prices) -1
            best_purchase_prices = [prices[0]]
            for i in range(1, len(prices)):
                if prices[i] <= best_purchase_prices[-1]:
                    best_purchase_prices.append(prices[i])
                else:
                    best_purchase_prices.append(best_purchase_prices[-1])
            
            # look for the best deal
            best = -10 ** 5
            for i in range(len(prices)):
                best = max(prices[i] - best_purchase_prices[i], best)
            
            return best
