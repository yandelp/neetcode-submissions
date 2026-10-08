class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for d in range(len(prices)):
            for s in range(d+1, len(prices)):
                if prices[s] - prices[d] > profit:
                    profit = prices[s] - prices[d]
                print(prices[d], prices[s], profit)
        return profit