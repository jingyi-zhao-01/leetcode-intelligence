# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-subarray-with-or-at-least-k-i
# source_path: LeetCode-Solutions-master/Python/shortest-subarray-with-or-at-least-k-i.py
# solution_class: Solution2
# submission_id: fbd7a6760faca2f4418ce41809bb0a49df937b40
# seed: 39298646

# Time:  O(nlogr) = O(n * 30)
# Space: O(logr) = O(30)

# freq table, two pointers

class Solution2(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = float("inf")
        for left in xrange(len(nums)):
            curr = 0
            for right in xrange(left, len(nums)):
                curr |= nums[right]
                if curr < k:
                    continue
                result = min(result, right-left+1)
                break
        return result if result != float("inf") else -1