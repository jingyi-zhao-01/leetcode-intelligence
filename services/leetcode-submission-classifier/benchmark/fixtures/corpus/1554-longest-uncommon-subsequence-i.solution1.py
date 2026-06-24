# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-uncommon-subsequence-i
# source_path: LeetCode-Solutions-master/Python/longest-uncommon-subsequence-i.py
# solution_class: Solution
# submission_id: dfa311b06826eff193fa68e20bdd375fdac40692
# seed: 1592029217

# Time:  O(min(a, b))
# Space: O(1)

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))