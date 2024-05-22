class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. Keeping the price as the price of the stock and first day
        2. Initialize the value at 0
        3. Check if there is a minimum price that was there 
        4. Check if we subtract it with the currect price can we get the max Value
        """
        min_value=prices[0]
        max_val=0
        for i in range(1,len(prices)):
            min_value=min(prices[i],min_value)
            max_val=max(prices[i]-min_value, max_val)
        return max_val

def main():
    arr=sys.stdin.read().strip()
    nums=list(map(int, arr.strip('[]').split(',')))
    sol=Solution()
    max_profit=sol.maxProfit(nums)
    print(max_profit)

if __name__=="__main__":
    main()