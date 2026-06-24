# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sum-of-mountain-triplets-i
# source_path: LeetCode-Solutions-master/Python/minimum-sum-of-mountain-triplets-i.py
# solution_class: Solution2
# submission_id: 42d073c7df9d36a5ec435c37939ec1843391bcf2
# seed: 1996194610

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution2(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INF = float("inf")

        left = [INF]*len(nums)
        curr = INF
        for i in xrange(len(nums)):
            left[i] = curr
            curr = min(curr, nums[i])
        right = [INF]*len(nums)
        curr = INF
        for i in reversed(xrange(len(nums))):
            right[i] = curr
            curr = min(curr, nums[i])
        result = INF
        for i in xrange(len(nums)):
            if left[i] < nums[i] > right[i]:
                result = min(result, left[i]+nums[i]+right[i])
        return result if result != INF else -1