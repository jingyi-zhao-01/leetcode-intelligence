# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-lines-to-write-string
# source_path: LeetCode-Solutions-master/Python/number-of-lines-to-write-string.py
# solution_class: Solution
# submission_id: 6132a4990e3a961cedd90a75deb864fa1f377be6
# seed: 3938501553

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        result = [1, 0]
        for c in S:
            w = widths[ord(c)-ord('a')]
            result[1] += w
            if result[1] > 100:
                result[0] += 1
                result[1] = w
        return result