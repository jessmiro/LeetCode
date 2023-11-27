# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        temp = head
        prev = temp
        count = 0

        # if it's empty, we return it empty
        if temp is None:
            return head;

        
        # otherwise if there's stuff in the list
        while temp is not None:
            # if the head is a value, we remove it
            # and then start the loop over
            if head.val is val:
                head = head.next
                temp = head
                continue

            # if there's nothing next, we leave
            if temp.next is None:
                break;
            
            #then we make prev the current
            prev = temp

            # because if the next value is what we're looking for
            if temp.next.val is val:
                #we point the current node (which is prev) to the next next node
                #skipping over the next node
                prev.next = temp.next.next
                continue
                
            #change temp
            temp = temp.next
        
        #and now we point to head and return head
        temp = head
        return head
        #if temp.val is val:
            #prev.next = None
            #return head
        #print("here's temp val: ", temp.val)
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
