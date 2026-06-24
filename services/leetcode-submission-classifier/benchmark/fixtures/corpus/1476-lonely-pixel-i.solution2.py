# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lonely-pixel-i
# source_path: LeetCode-Solutions-master/Python/lonely-pixel-i.py
# solution_class: Solution2
# submission_id: c0d0fe0552e66ece9f82ce3f776be2d70120f071
# seed: 4041659849

# Time:  O(m * n)
# Space: O(m + n)

class Solution2(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') \
               for col in zip(*picture))