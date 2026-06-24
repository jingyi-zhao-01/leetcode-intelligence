# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-function
# source_path: LeetCode-Solutions-master/Python/rotate-function.py
# solution_class: Solution
# submission_id: 1e41b70acd0ad2c36886a4b20775c19f4a6c5bbb
# seed: 3596343705

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = sum(A)
        fi = 0
        for i in xrange(len(A)):
            fi += i * A[i]

        result = fi
        for i in xrange(1, len(A)+1):
            fi += s - len(A) * A[-i]
            result = max(result, fi)
        return result