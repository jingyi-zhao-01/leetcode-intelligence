# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-unique-even-element
# source_path: LeetCode-Solutions-master/Python/first-unique-even-element.py
# solution_class: Solution
# submission_id: 37eb91aea73cc6607fe3d723bcc3f8a811657672
# seed: 872020473

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
        for x in nums:
            if x%2 == 0 and cnt[x] == 1:
                return x
        return -1