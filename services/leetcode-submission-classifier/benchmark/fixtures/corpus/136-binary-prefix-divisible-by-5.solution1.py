# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-prefix-divisible-by-5
# source_path: LeetCode-Solutions-master/Python/binary-prefix-divisible-by-5.py
# solution_class: Solution
# submission_id: 71517ae3b0f99e12b9f534c118ec16584e890850
# seed: 1955679946

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        for i in xrange(1, len(A)):
            A[i] += A[i-1] * 2 % 5
        return [x % 5 == 0 for x in A]