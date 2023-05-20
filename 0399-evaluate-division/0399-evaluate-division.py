class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj=collections.defaultdict(list)
        for i,q in enumerate(equations):
            a,b=q
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])

        def bfs(src,target):
            if src not in adj or target not in adj:
              return -1.0
            q,visited=deque(),set()
            q.append([src,1])
            visited.add(src)
            while q:
              n,w=q.popleft()
              if n==target:
                return w 
              for nei,weight in adj[n]:
                if nei not in visited:
                  q.append([nei,w*weight])
                  visited.add(nei)
            return -1.0 
        return([bfs(q[0],q[1])for q in queries])