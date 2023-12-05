# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        prev_val = 0
        prev = head
        curr = head

        if curr is None:
            return head;

        if curr.next is None:
            return head;
        
        # otherwise if there's stuff in the list
        while curr is not None:
            # if the head is a value, we remove it
            # and then start the loop over
           

            # if there's nothing next, we leave
            if curr.next is None:
                break;
            
            

           
            

            # because if the next value is what we're looking for
            if curr.val == prev_val:
                #we point the current node (which is prev) to the next next node
                #skipping over the next node
                prev.next = curr.next
                curr = curr.next
                continue
                


            # now we just do one last prev check
            prev_val = curr.val
            prev = curr
            
            curr = curr.next
        
        #if previous is the same as the last node
        #we remove the current node
        if curr.val == prev_val:
            prev.next = None
        
        
        #and now we point to head and return head
        curr = head
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
