# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-number-of-k-sum-pairs
# source_path: LeetCode-Solutions-master/Python/max-number-of-k-sum-pairs.py
# solution_class: Solution
# submission_id: 0baad6643ec4ce56542804a6209711703cc37878
# seed: 516842971

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        result = 0
        for x in nums:
            if k-x in count and count[k-x]:
                count[k-x] -= 1
                result += 1
            else:
                count[x] += 1
        return result