class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        mod = 10**9 + 7
        dp ={0:1}
        sum=0
        for i in range(1,high+1):
            if i-zero>=0:
              x=dp[i-zero]
            else:
              x=0
            if i-one>=0:
              y=dp[i-one]
            else:
              y=0    
            z=(x+y)%mod
            dp[i]=z
        for i in range(low,high+1):
            sum+=dp[i] % mod
        return sum % mod