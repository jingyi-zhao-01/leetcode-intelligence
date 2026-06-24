# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: similar-rgb-color
# source_path: LeetCode-Solutions-master/Python/similar-rgb-color.py
# solution_class: Solution
# submission_id: a0689d581b3989020732a96610ea85790e586e9b
# seed: 464217057

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def rounding(color):
            q, r = divmod(int(color, 16), 17)
            if r > 8: q += 1
            return '{:02x}'.format(17*q)

        return '#' + \
                rounding(color[1:3]) + \
                rounding(color[3:5]) + \
                rounding(color[5:7])