class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.nums=nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[(self.k)-1]
        


# # Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)