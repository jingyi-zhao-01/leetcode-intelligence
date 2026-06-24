# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-anagram-mappings
# source_path: LeetCode-Solutions-master/Python/find-anagram-mappings.py
# solution_class: Solution
# submission_id: b250eb12d1adff7bbed8934dfc0819d868aa2769
# seed: 4241615404

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        lookup = collections.defaultdict(collections.deque)
        for i, n in enumerate(B):
            lookup[n].append(i)
        result = []
        for n in A:
            result.append(lookup[n].popleft())
        return result