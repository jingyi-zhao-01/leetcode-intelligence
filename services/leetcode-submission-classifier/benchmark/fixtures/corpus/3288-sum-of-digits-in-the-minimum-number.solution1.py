# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-digits-in-the-minimum-number
# source_path: LeetCode-Solutions-master/Python/sum-of-digits-in-the-minimum-number.py
# solution_class: Solution
# submission_id: eb40787a8bac5b27ca071d205ad7b76d715a2fcd
# seed: 1331609134

# Time:  O(n * l)
# Space: O(l)

class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = sum([int(c) for c in str(min(A))])
        return 1 if total % 2 == 0 else 0