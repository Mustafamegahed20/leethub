class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        colors = [-1] * len(graph)
        for v in range(len(graph)):
            if colors[v] == -1:
                stack = [v]
                colors[v] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if colors[nei] == colors[node]:
                            return False
                        if colors[nei] == -1:
                            colors[nei] = colors[node] ^ 1
                            stack.append(nei)       
        return True