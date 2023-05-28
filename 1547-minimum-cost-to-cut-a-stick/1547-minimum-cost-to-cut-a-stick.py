class Solution(object):
    def minCost(self, n, A):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        A = sorted(A + [0, n])
        k = len(A)
        dp = [[0] * k for _ in xrange(k)]
        for d in xrange(2, k):
            for i in xrange(k - d):
                dp[i][i + d] = min(dp[i][m] + dp[m][i + d] for m in xrange(i + 1, i + d)) + A[i + d] - A[i]
        return dp[0][k - 1]