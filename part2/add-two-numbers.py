# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

      #make two empty strings
        x = ""
        y = ""

      #iterate through both to collect values
        while l1.next:
            x = x + str(l1.val)
            l1 = l1.next
        #flip them
        x = (x + str(l1.val))[::-1]

      #same as l1
        while l2.next:
            y = y + str(l2.val)
            l2 = l2.next
            
        y = (y + str(l2.val))[::-1]

      #now we add them and concert to a string so we can make it into a list
        summing = int(y) +int(x)
        summing = str(summing)

        sumList = list(summing)

      # we add to the front so we just need to keep adding the first value in the list
      #this is for the head
        head = ListNode(sumList[0])
        sumList.pop(0)


        curr = head
       

      #now we go through the list to add the new value to the front of the list
      #this also hits the "must be added backwards" issue
        while sumList: 
                curr = ListNode(sumList[0])
                curr.next = head
                head = curr
                sumList.pop(0)
        
        return curr

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
