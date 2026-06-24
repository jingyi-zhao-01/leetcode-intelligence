# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-number-after-mutating-substring
# source_path: LeetCode-Solutions-master/Python/largest-number-after-mutating-substring.py
# solution_class: Solution
# submission_id: 9b7cffe9d1907f5b51caf26a459d3a160b3a1ee8
# seed: 4113586993

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        mutated = False
        result = map(int, list(num))
        for i, d in enumerate(result):
            if change[d] < d:
                if mutated:
                    break
            elif change[d] > d:
                result[i] = str(change[d])
                mutated = True
        return "".join(map(str, result))