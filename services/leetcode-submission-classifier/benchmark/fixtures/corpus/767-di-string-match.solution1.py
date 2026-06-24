# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: di-string-match
# source_path: LeetCode-Solutions-master/Python/di-string-match.py
# solution_class: Solution
# submission_id: 197b94b4b7e499b6b89febe955232bfcdfa00acd
# seed: 3621390660

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        left, right = 0, len(S)
        for c in S:
            if c == 'I':
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        result.append(left)
        return result