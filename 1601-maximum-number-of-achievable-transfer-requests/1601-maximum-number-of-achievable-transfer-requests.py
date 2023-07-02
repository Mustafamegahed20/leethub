class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        tot = len(requests)
        for i in range(tot, 0, -1):
            comb = list(itertools.combinations([j for j in range(tot)], i))
            for c in comb:
                net = [0 for j in range(n)]
                for idx in c:
                    net[requests[idx][0]] -= 1
                    net[requests[idx][1]] += 1
                if net == [0 for j in range(n)]:
                    return i
        return 0