# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        listVal = []
        curr = head
        
        #go through the linked list and append it to the created list
        while curr != None:
            listVal.append(curr.val)
            curr = curr.next

        # reverse the list and store it
        listValRev = listVal[::-1]

        # if it's the same, it's a palindrome 
        if(listVal == listValRev):
            return True
        """
        :type head: ListNode
        :rtype: bool
        """
        
