class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        suffix_sums = [0] * (n + 1)
        suffix_sums[n - 1] = piles[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]

        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sums[i]
                else:
                    for x in range(1, 2 * m + 1):
                        opponent_score = dp[i + x][max(x, m)]
                        score = suffix_sums[i] - opponent_score
                        dp[i][m] = max(dp[i][m], score)
        
        return dp[0][1]