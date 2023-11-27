# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        #node is what we want to delete
        # so we copy the value from the next node to node
        node.val = node.next.val
        #now we assign the next node to toDel
        toDel = node.next
        #and the next node becomes the next next node
        node.next = node.next.next
        #so we just delete nodeNext
        del toDel
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
