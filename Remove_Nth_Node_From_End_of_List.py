# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Example:
        Given linked list: 1->2->3->4->5, and n = 2.
        After removing the second node from the end, the linked list becomes 1->2->3->5.
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
            
        if(not fast):
            return(head.next)
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return(head)
        

   
