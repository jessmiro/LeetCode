# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):

        # I actually couldn't get this one to submit but I have the general idea down
        # If it's an empty or length of 1 list
        if head is None or head.next is None:
            return head

        # now we have a left and right Node for the pair
        left = head
        right = head.next

        #checking to make sure we have left and left next
        while left is not None and left.next is not None :
            # left now points to where right is pointing
            left.next = right.next
            # and right now points to left
            right.next = left
            # now we move left over to next
            left = left.next

            
            # And technically, right is moved to the right of left
            #however I keep getting errors that left.next is incorrect
            # So in the future, I'll work on fixing that. 
            if left != None or left.next != None:  
                right = left.next
        
        
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
