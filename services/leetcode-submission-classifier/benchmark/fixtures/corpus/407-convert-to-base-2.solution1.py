# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-to-base-2
# source_path: LeetCode-Solutions-master/Python/convert-to-base-2.py
# solution_class: Solution
# submission_id: 2eaf0951cd1b68e3537ce21d5e04c7ddea3a3e45
# seed: 412913346

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        result = []
        while N:
            result.append(str(-N & 1))  # N % -2
            N = -(N >> 1)  # N //= -2
        result.reverse()
        return "".join(result) if result else "0"