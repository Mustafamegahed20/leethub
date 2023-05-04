from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        radiant = deque()
        dire = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
        return "Radiant" if radiant else "Dire"
