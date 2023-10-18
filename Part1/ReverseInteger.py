class Solution(object):
    def reverse(self, x):
        #we change x to a string and reverse
        xStrR = (str(x))[::-1]

        #deal with neg here
        if (xStrR[-1] == '-'):
            #remove neg
            xStrR = xStrR.strip("-")
            #than add it back to the front
            xStrR = '-' + xStrR

        #check bit int
        if(int(xStrR) > (2 ** 31 - 1) or int(xStrR) < (-2**31)):
            #too big or too small return 0
            return 0

        #then we return int of xStrR
        return int(xStrR)
        """
        :type x: int
        :rtype: int
        """
        
