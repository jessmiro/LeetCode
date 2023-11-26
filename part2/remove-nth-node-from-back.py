# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        counter = 0

        #get where the node to be deleted is
        while(temp):
            counter = counter + 1
            temp = temp.next
        
        #reset temp
        #get the spot, reset count
        temp = head
        spot = counter - n
        counter = 0
        
        #if spot is 0, then we get rid of head and return it
        if counter == spot:
            head = head.next
            return head

        # otherwise we go to the node before the node to delete
        while counter  < (spot - 1):            
            counter = counter + 1
            temp = temp.next
        
        
        #now we set the next of the node before note do be deleted to be the next of next 
        temp.next = temp.next.next
    
        #return head
        return head

        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
