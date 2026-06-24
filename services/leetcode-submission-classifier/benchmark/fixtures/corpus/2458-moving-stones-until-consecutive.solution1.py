# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: moving-stones-until-consecutive
# source_path: LeetCode-Solutions-master/Python/moving-stones-until-consecutive.py
# solution_class: Solution
# submission_id: d5443f9079bca30c20f39b21cb8d1eb72e8ce6a0
# seed: 4198900652

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        s = [a, b, c]
        s.sort()
        if s[0]+1 == s[1] and s[1]+1 == s[2]:
            return [0, 0]
        return [1 if s[0]+2 >= s[1] or s[1]+2 >= s[2] else 2, s[2]-s[0]-2]