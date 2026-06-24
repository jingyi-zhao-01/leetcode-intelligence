# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: top-k-frequent-elements
# source_path: LeetCode-Solutions-master/Python/top-k-frequent-elements.py
# solution_class: Solution
# submission_id: e0b973b6ee2617848dd5f161c708ec3a2b130cab
# seed: 3897126021

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        buckets = [[] for _ in xrange(len(nums)+1)]
        for i, count in counts.iteritems():
            buckets[count].append(i)

        result = []
        for i in reversed(xrange(len(buckets))):
            for j in xrange(len(buckets[i])):
                result.append(buckets[i][j])
                if len(result) == k:
                    return result
        return result