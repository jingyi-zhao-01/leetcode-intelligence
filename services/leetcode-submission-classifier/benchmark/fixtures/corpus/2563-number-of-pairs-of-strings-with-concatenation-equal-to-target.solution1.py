# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-pairs-of-strings-with-concatenation-equal-to-target
# source_path: LeetCode-Solutions-master/Python/number-of-pairs-of-strings-with-concatenation-equal-to-target.py
# solution_class: Solution
# submission_id: d616d18d001471f6b29ad2beefa575d8250ca412
# seed: 3355701664

# Time:  O(n * l), n is the size of nums, l is the average length of the digit string in nums
# Space: O(n)

import collections

class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        lookup = collections.Counter()
        result = 0
        for num in nums:
            cnt1, cnt2 = lookup[-(len(target)-len(num))], lookup[len(target)-len(num)]
            if target.startswith(num):
                result += cnt1
                lookup[len(num)] += 1
            if target.endswith(num):
                result += cnt2
                lookup[-len(num)] += 1
        return result