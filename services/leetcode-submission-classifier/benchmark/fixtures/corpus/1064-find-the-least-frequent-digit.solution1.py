# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-least-frequent-digit
# source_path: LeetCode-Solutions-master/Python/find-the-least-frequent-digit.py
# solution_class: Solution
# submission_id: 2abf05daa4b665033e76008dfca6683a1be8b089
# seed: 2793731315

# Time:  O(logn + 10)
# Space: O(10)

# freq table

class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = [0]*10
        while n:
            n, r = divmod(n, 10)
            cnt[r] += 1
        mn = min(x for x in cnt if x)
        return next(i for i in range(len(cnt)) if cnt[i] == mn)