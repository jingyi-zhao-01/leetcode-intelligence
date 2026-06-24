# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-subsets
# source_path: LeetCode-Solutions-master/Python/word-subsets.py
# solution_class: Solution
# submission_id: bdb34189deaf720555e8231ecb19a3e3d9264986
# seed: 2117188758

# Time:  O(m + n)
# Space: O(1)

import collections

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        count = collections.Counter()
        for b in B:
            for c, n in collections.Counter(b).items():
                count[c] = max(count[c], n)
        result = []
        for a in A:
            count = collections.Counter(a)
            if all(count[c] >= count[c] for c in count):
                result.append(a)
        return result