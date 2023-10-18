class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        # add lists and sort and store to new var
        nums3S = sorted(nums1 + nums2)

        #here's our middle
        middle = len(nums3S)/2

        # if even
        if len(nums3S)%2 == 0:
            #we need to add the middles
            mids = nums3S[middle-1] + nums3S[middle]
            #and divide by 2 and then return
            mids = mids/2.0
            return mids

        #otherwise we just return the value of the middle
        return float(nums3S[middle])

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
