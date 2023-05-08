class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n=len(mat)-1
        sum=0
        for i in range(len(mat)):
            j = n - i
            if i==j:        
              sum+=mat[i][i]
            else:
                sum+=mat[i][i]+mat[i][j]
        return sum
        