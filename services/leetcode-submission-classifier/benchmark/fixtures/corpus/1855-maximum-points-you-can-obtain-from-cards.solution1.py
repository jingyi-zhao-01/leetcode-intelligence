# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-points-you-can-obtain-from-cards
# source_path: LeetCode-Solutions-master/Python/maximum-points-you-can-obtain-from-cards.py
# solution_class: Solution
# submission_id: 58ee6342a00fda91e9470771d44e9d128bc363cb
# seed: 3962179704

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        result, total, curr, left = float("inf"), 0, 0, 0
        for right, point in enumerate(cardPoints):
            total += point
            curr += point
            if right-left+1 > len(cardPoints)-k:
                curr -= cardPoints[left]
                left += 1
            if right-left+1 == len(cardPoints)-k:
                result = min(result, curr)
        return total-result