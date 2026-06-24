# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-the-longest-new-string
# source_path: LeetCode-Solutions-master/Python/construct-the-longest-new-string.py
# solution_class: Solution
# submission_id: 494fa4ffa8b0a10deca9a54a117c620060e270d0
# seed: 1053820369

# Time:  O(1)
# Space: O(1)

# constructive algorithms, math

class Solution(object):
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        return ((min(x, y)*2+int(x != y))+z)*2