class Solution(object):
    def isPalindrome(self, x):
        #change to palindrome
        xStr = str(x)
      #reverse
        xStrRev = xStr[::-1]
        #are they the same ? if yes, then true
        if(xStr == xStrRev):
            return True

        return False
        """
        :type x: int
        :rtype: bool
        """
        
