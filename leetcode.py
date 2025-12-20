# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    new_head = None
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def helper(head):
            if not head:
                return 
            if not head.next:
                self.new_head = head
                return head

            next_pointer = helper(head.next)
            next_pointer.next = head
            head.next = None

            return head 
        
        final = helper(head)
        return self.new_head
    

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """ 
       
        front = head

        if head and head.next:
            head = head.next

        while (not head or not head.next):

            decoupled = head.next

            head.next = front

            front = head

            head = decoupled
        
        head.next = front
        front = head

        return front
            
            




        
