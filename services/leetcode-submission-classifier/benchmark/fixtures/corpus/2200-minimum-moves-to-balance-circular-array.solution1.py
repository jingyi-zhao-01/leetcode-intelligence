# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-balance-circular-array
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-balance-circular-array.py
# solution_class: Solution
# submission_id: fac0a5f61b2a1ca63b752dadf0470f587775a76e
# seed: 379498670

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minMoves(self, balance):
        """
        :type balance: List[int]
        :rtype: int
        """
        i = next((i for i in xrange(len(balance)) if balance[i] < 0), len(balance))
        if i == len(balance):
            return 0
        if sum(balance) < 0:
            return -1
        result = 0
        for d in xrange(1, len(balance)//2+1):
            c = min(balance[(i+d)%len(balance)]+balance[(i-d)%len(balance)], -balance[i])
            result += c*d
            balance[i] += c
            if not balance[i]:
                break
        return result