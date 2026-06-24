# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-array-continuous
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-array-continuous.py
# solution_class: Solution2
# submission_id: 79df9abfcb059fc3ab1fd33e1352b034a1534d1f
# seed: 100838877

# Time:  O(nlogn)
# Space: O(1)

class Solution2(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(set(nums))
        result = right = 0
        for left in xrange(len(nums)):
            while right < len(nums) and nums[right] <= nums[left]+n-1:
                right += 1
            result = max(result, right-left)
        return n-result