# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        
        while curr and curr.next:
            #save_pointer
            nextpair=curr.next.next
            second=curr.next
            
            #reverse_pair
            second.next=curr
            curr.next=nextpair
            prev.next=second
            
            ##update
            prev=curr
            curr=nextpair
            
        return dummy.next
            
            
            