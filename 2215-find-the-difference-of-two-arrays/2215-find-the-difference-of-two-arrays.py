class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        hashtable_1 = {}
        hashtable_2 = {}

        for element in nums1:
            hashtable_1[element] = True

        for element in nums2:
            hashtable_2[element] = True

        for element in nums2:
            if element in hashtable_1:
                del hashtable_1[element]

        for element in nums1:
          if element in hashtable_2:
                del hashtable_2[element]
        output=[]
        output.append(list(hashtable_1.keys()))
        output.append(list(hashtable_2.keys()))
        return output