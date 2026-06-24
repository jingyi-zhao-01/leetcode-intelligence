# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-different-subsequences-gcds
# source_path: LeetCode-Solutions-master/Python/number-of-different-subsequences-gcds.py
# solution_class: Solution
# submission_id: 4a870a4a18dbdeb47f77713028df653c9e0f60ac
# seed: 1941098418

# Time:  O(n + m * (1 + 1/2 + 1/3 + ... + 1/m)) = O(n + mlogm), m is max of nums
# Space: O(n)

import fractions

class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num, nums_set = max(nums), set(nums)
        result = 0
        for i in xrange(1, max_num+1):
            d = 0
            for x in xrange(i, max_num+1, i):
                if x not in nums_set:
                    continue
                d = fractions.gcd(d, x)  # total time: O(log(min(d, x)) = O(logd), where d keeps the same or gets smaller
                if d == i:
                    result += 1
                    break
        return result