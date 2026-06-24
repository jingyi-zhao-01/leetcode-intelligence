# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-array-pairs-are-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/check-if-array-pairs-are-divisible-by-k.py
# solution_class: Solution
# submission_id: 364834b8c1f83c410f5256b35cdba53bd22eec14
# seed: 1982472307

# Time:  O(n)
# Space: O(k)

import collections

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        count = collections.Counter(i%k for i in arr)
        return (0 not in count or not count[0]%2) and \
                all(k-i in count and count[i] == count[k-i] for i in xrange(1, k) if i in count)