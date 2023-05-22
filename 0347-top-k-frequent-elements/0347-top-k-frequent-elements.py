class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_freq[i][0])
        return result