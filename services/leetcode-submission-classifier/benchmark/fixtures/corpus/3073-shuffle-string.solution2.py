# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shuffle-string
# source_path: LeetCode-Solutions-master/Python/shuffle-string.py
# solution_class: Solution2
# submission_id: 219a836c91935cc5045086cd32487ab34fc1210b
# seed: 3605406056

# Time:  O(n)
# Space: O(1)

# in-place solution

class Solution2(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result = ['']*len(s)
        for i, c in itertools.izip(indices, s):
            result[i] = c
        return "".join(result)