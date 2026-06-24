# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-colored-pieces-if-both-neighbors-are-the-same-color
# source_path: LeetCode-Solutions-master/Python/remove-colored-pieces-if-both-neighbors-are-the-same-color.py
# solution_class: Solution
# submission_id: 1a1449e8a2353335bdd6bbfcb7e10a5bbb17f80a
# seed: 2195126559

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        cnt1 = cnt2 = 0
        for i in xrange(1, len(colors)-1):
            if not (colors[i-1] == colors[i] == colors[i+1]):
                continue
            if colors[i] == 'A':
                cnt1 += 1
            else:
                cnt2 += 1
        return cnt1 > cnt2