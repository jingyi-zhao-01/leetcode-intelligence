# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: collecting-chocolates
# source_path: LeetCode-Solutions-master/Python/collecting-chocolates.py
# solution_class: Solution3
# submission_id: be23e305e4c993679e2801b5782af772876323bd
# seed: 1462331121

# Time:  O(n)
# Space: O(n)

# mono stack, difference array, prefix sum

class Solution3(object):
    def minCost(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        result = [x*k for k in xrange(len(nums)+1)]
        for i in xrange(len(nums)):
            curr = nums[i]
            for k in xrange(len(result)):
                curr = min(curr, nums[(i+k)%len(nums)])
                result[k] += curr
        return min(result)