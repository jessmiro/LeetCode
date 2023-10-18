class Solution(object):
    def twoSum(self, nums, target):
        #for each item in nums
        for i in range(len(nums)):
            #we create a var that's the target - value of current index
            matchNo = target - nums[i]

            #then we check if the matching number is in the list
            #AND we check to make sure we don't return the same index twice
            if matchNo in nums and (i != nums.index(matchNo)):
                #then we return i and the index of the matching number
                return [i, nums.index(matchNo)]
            else:
                #if matchNo isnt in nums or i does match the index of matchNo
                #we continue
                continue

        #otherwise, we return an empty list
        return []   

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
