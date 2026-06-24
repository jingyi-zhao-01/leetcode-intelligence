# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: top-k-frequent-elements
# source_path: LeetCode-Solutions-master/Python/top-k-frequent-elements.py
# solution_class: Solution3
# submission_id: 7b4043619d022a4b8465fbf72864179d32a46388
# seed: 763014957

# Time:  O(n)
# Space: O(n)

import collections

class Solution3(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [key for key, _ in collections.Counter(nums).most_common(k)]