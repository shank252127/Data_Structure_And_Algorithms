class Solution:
    
    def solve(self, A):
        coinVal = 1       
        noOfCoins = 0        
        diff = A

        while diff != 0:
            # If coin value is less diff ( equals to remaining amount needed to add up to total cost)
            if(coinVal <= diff):
                coinVal = coinVal*5
            else:
                coinVal = coinVal//5
                if(coinVal > diff):
                    continue  
                # Only possible when coinval < diff   
                noOfCoins = noOfCoins+ 1
                diff = diff-coinVal
            
        return noOfCoins

a = Solution()
ans = a.solve(2011)
print(ans)
