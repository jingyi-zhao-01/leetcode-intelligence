# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-frequent-number-following-key-in-an-array
# source_path: LeetCode-Solutions-master/Python/most-frequent-number-following-key-in-an-array.py
# solution_class: Solution
# submission_id: cecd4819957257ed2d1e81a6b07880959ea1ee48
# seed: 1110648499

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        return collections.Counter(nums[i+1] for i in xrange(len(nums)-1) if nums[i] == key).most_common(1)[0][0]