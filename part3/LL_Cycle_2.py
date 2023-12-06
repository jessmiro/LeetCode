# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slowP = head
        fastP = head
        count = 0

        

        #we need to make sure fastP and fastP next aren't None
        while fastP is not None and fastP.next is not None:
            # slow goes by 1
            slowP = slowP.next
            #fast goes by 2
            fastP = fastP.next.next
            count = count + 1
           
            
            #if there's a loop, they eventually meet up
            #this one doesn't work for a few instances but the general
            # idea is still there
            if(slowP == fastP):
                print("yes")
                print("count: ", count)
                return fastP.next.next
            continue
            
            
        return None
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
