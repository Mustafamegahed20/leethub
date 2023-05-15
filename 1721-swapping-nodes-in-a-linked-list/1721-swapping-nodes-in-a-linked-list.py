# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # Check if k is valid
        if k > n or k < 1:
            return head

        # Find the kth node from the beginning
        node_k_from_beginning = head
        for i in range(k-1):
            node_k_from_beginning = node_k_from_beginning.next

        # Find the kth node from the end
        node_k_from_end = head
        for i in range(n-k):
            node_k_from_end = node_k_from_end.next

        # Swap the values of the nodes
        node_k_from_beginning.val, node_k_from_end.val = node_k_from_end.val, node_k_from_beginning.val

        return head
        
        