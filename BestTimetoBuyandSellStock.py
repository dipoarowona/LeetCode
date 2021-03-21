class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        last_price = -1
        maxx= -1
        buy = 0
        sell = 0
        profit = 0
        open_trade = False
        for i in range(len(prices)):
            if last_price<prices[i] and not open_trade and last_price!=-1:
                buy = last_price
                open_trade = True
            if last_price>prices[i] and open_trade and last_price!=-1:
                sell = last_price
                open_trade = False
                profit += sell-buy
            last_price = prices[i]
        return profit if not open_trade else profit + prices[-1]-buy
