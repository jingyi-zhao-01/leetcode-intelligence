# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bag-of-tokens
# source_path: LeetCode-Solutions-master/Python/bag-of-tokens.py
# solution_class: Solution
# submission_id: 61c28cb52a4148d7d395767083e637db9edbf835
# seed: 2740148657

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        result, points = 0, 0
        left, right = 0, len(tokens)-1
        while left <= right:
            if P >= tokens[left]:
                P -= tokens[left]
                left += 1
                points += 1
                result = max(result, points)
            elif points > 0:
                points -= 1
                P += tokens[right]
                right -= 1
            else:
                break
        return result