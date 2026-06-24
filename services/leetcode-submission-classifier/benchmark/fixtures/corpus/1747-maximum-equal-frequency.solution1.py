# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-equal-frequency
# source_path: LeetCode-Solutions-master/Python/maximum-equal-frequency.py
# solution_class: Solution
# submission_id: 987e824725140fe02b76abe33cdf2e6166bd5f95
# seed: 1603858184

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        count = collections.Counter()
        freq = [0 for _ in xrange(len(nums)+1)]
        for i, n in enumerate(nums, 1):
            freq[count[n]] -= 1
            freq[count[n]+1] += 1
            count[n] += 1
            c = count[n]
            if freq[c]*c == i and i < len(nums):
                result = i+1
            remain = i-freq[c]*c
            if freq[remain] == 1 and remain in [1, c+1]:
                result = i
        return result