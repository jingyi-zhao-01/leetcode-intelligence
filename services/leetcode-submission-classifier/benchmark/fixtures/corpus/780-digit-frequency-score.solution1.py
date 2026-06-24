# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: digit-frequency-score
# source_path: LeetCode-Solutions-master/Python/digit-frequency-score.py
# solution_class: Solution
# submission_id: 9804f686ef5458e0eb2756df93e0ccfa933fe78d
# seed: 648614047

# Time:  O(logn)
# Space: O(1)

# freq table

class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = [0]*10
        while n:
            n, r = divmod(n, 10)
            cnt[r] += 1
        return sum(i*x for i, x in enumerate(cnt))