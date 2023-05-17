# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        values = []
        current = head
        n = 0
        while current:
            values.append(current.val)
            current = current.next
            n += 1

        # Sort the values in ascending order
        # values.sort()

        # Compute the maximum twin sum
        max_sum = 0
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_sum = max(max_sum, twin_sum)

        return max_sum
        
            