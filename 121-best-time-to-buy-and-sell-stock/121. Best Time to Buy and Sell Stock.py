class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through prices list with left and right pointer 0 and 1 respectively
        # have a maxprofit defaulted to 0 before iteration
        # while r < len(prices) check if left is smaller than right
        # if l < r get max between current profit and max profit
        # else update l to be r and then increment r
        l, r = 0, 1
        maxprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxprofit = max(maxprofit, prices[r] - prices[l])
            else:
                l = r
            r+=1
        
        return maxprofit

        # Time Complexity: O(n)
        # Space Complexity: O(1)