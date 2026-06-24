# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shuffle-string
# source_path: LeetCode-Solutions-master/Python/shuffle-string.py
# solution_class: Solution
# submission_id: 038d2119caa80788dc026ae54012dfdd02bfdba8
# seed: 2559172692

# Time:  O(n)
# Space: O(1)

# in-place solution

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result = list(s)
        for i, c in enumerate(result):
            if indices[i] == i:
                continue
            move, j = c, indices[i]
            while j != i:
                result[j], move = move, result[j]
                indices[j], j = j, indices[j]
            result[i] = move
        return "".join(result)