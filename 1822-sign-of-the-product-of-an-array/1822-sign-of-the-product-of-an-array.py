class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product=1
        for i in range (len(nums)):
           product=product*nums[i]
        if product >0:
           x=1
        elif product <0:
          x=-1
        else:
          x=0
        return x
        