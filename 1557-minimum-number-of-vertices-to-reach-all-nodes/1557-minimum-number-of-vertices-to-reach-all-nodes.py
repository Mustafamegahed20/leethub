class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        #Setting graph 
        reachable=set()  
        vertices=set(range(n))


        for i in range(len(edges)):
            reachable.add(edges[i][1])

        x=vertices-reachable

        return x