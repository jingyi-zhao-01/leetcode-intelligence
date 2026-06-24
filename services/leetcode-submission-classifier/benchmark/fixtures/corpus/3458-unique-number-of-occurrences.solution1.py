# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-number-of-occurrences
# source_path: LeetCode-Solutions-master/Python/unique-number-of-occurrences.py
# solution_class: Solution
# submission_id: d4efe1068a5e4b2ee4115467b4871aa43c9c63d6
# seed: 3840234618

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = collections.Counter(arr)
        lookup = set()
        for v in count.itervalues():
            if v in lookup:
                return False
            lookup.add(v)
        return True