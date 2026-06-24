# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-frequency-of-an-element-after-performing-operations-i
# source_path: LeetCode-Solutions-master/Python/maximum-frequency-of-an-element-after-performing-operations-i.py
# solution_class: Solution2
# submission_id: 81e74ca7364acb4bd947be78147334546d2b891f
# seed: 1128678467

# Time:  O(nlogn)
# Space: O(n)

import collections


# sort, freq table, two pointers, sliding window

class Solution2(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        cnt = collections.defaultdict(int)  # defaultdict is much faster than Counter
        for x in nums:
            cnt[x] += 1
        diff = defaultdict(int)
        for x in nums:
            diff[x] += 0
            diff[x-k] += 1
            diff[x+k+1] -= 1
        result = curr = 0
        for x, c in sorted(diff.iteritems()):
            curr += c
            result = max(result, cnt[x]+min(curr-cnt[x], numOperations))
        return result