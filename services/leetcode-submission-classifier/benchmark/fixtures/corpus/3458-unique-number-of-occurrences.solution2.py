# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-number-of-occurrences
# source_path: LeetCode-Solutions-master/Python/unique-number-of-occurrences.py
# solution_class: Solution2
# submission_id: 88ca748939975a794387369614c9e00e599723df
# seed: 97114499

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = collections.Counter(arr)
        return len(count) == len(set(count.itervalues()))