# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: set-mismatch
# source_path: LeetCode-Solutions-master/Python/set-mismatch.py
# solution_class: Solution2
# submission_id: 02478a923d53e18ec58dac11122bc756d1f389fa
# seed: 1833302295

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * 2
        for i in nums:
            if nums[abs(i)-1] < 0:
                result[0] = abs(i)
            else:
                nums[abs(i)-1] *= -1
        for i in xrange(len(nums)):
            if nums[i] > 0:
                result[1] = i+1
            else:
                nums[i] *= -1
        return result