# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: majority-element
# source_path: LeetCode-Solutions-master/Python/majority-element.py
# solution_class: Solution2
# submission_id: ebee4326e9c09e294e5963f990acc9baa1516a28
# seed: 2212977980

# Time:  O(n)
# Space: O(1)

import collections

class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return collections.Counter(nums).most_common(1)[0][0]