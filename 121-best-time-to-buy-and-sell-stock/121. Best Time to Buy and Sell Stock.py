class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_area = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                max_area = max(max_area, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return max_area