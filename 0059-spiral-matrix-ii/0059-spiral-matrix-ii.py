class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for j in range(n)] for i in range(n)]

        up,down=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        m=1
        while up <= down and left <=right:

            for i in range(left,right+1):
              matrix[up][i]=m
              m+=1
            up+=1

            for i in range(up,down+1):
                matrix[i][right]=m
                m+=1
            right-=1

            if up <= down:
                for i in range(right,left-1,-1):
                    matrix[down][i]=m
                    m+=1
                down-=1


            for i in range(down,up-1,-1):
                matrix[i][left]=m
                m+=1
            left+=1 
        return matrix