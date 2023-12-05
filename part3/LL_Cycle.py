# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # set up fast and slow pointers

        slowP = head
        fastP = head

        #we need to make sure fastP and fastP next aren't None
        while fastP and fastP.next:
            # slow goes by 1
            slowP = slowP.next
            #fast goes by 2
            fastP = fastP.next.next

            #if there's a loop, they eventually meet up
            if(slowP == fastP):
                return True

            
            
        """
        :type head: ListNode
        :rtype: bool
        """
        
