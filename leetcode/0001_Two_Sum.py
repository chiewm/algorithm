# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idxDict = dict()
        for idx, num in enumerate(nums):
            if target - num in idxDict:
                return [idxDict[target - num], idx]
            idxDict[num] = idx

