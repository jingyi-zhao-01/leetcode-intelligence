# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-array-in-sets-of-k-consecutive-numbers
# source_path: LeetCode-Solutions-master/Python/divide-array-in-sets-of-k-consecutive-numbers.py
# solution_class: Solution
# submission_id: 66d2cb223d37a08393c477876002ebab554b28ea
# seed: 3517437166

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = collections.Counter(nums)
        for num in sorted(count.keys()):
            c = count[num]
            if not c:
                continue
            for i in xrange(num, num+k):
                if count[i] < c:
                    return False
                count[i] -= c
        return True