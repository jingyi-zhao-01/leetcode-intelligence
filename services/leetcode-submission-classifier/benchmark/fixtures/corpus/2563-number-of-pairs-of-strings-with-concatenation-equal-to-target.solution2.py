# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-pairs-of-strings-with-concatenation-equal-to-target
# source_path: LeetCode-Solutions-master/Python/number-of-pairs-of-strings-with-concatenation-equal-to-target.py
# solution_class: Solution2
# submission_id: 5b22e0881b9520e41a8e9ebec96bbd4723f65d3a
# seed: 14177467

# Time:  O(n * l), n is the size of nums, l is the average length of the digit string in nums
# Space: O(n)

import collections

class Solution2(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        prefix, suffix = collections.Counter(), collections.Counter()
        result = 0
        for num in nums:
            if target.startswith(num):
                result += suffix[len(target)-len(num)]
            if target.endswith(num):
                result += prefix[len(target)-len(num)]
            if target.startswith(num):
                prefix[len(num)] += 1
            if target.endswith(num):
                suffix[len(num)] += 1
        return result