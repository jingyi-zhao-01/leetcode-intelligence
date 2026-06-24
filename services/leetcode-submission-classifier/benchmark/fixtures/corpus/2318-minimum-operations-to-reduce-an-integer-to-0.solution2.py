# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-reduce-an-integer-to-0
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-reduce-an-integer-to-0.py
# solution_class: Solution2
# submission_id: a40941cb5bad9b5d0d7e4f386a19d3ea05f859a0
# seed: 78182049

# Time:  O(logn)
# Space: O(1)

# greedy, trick
# reference: https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/solutions/3203994/java-c-python-1-line-solution/

class Solution2(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            if n&1:
                n >>= 1
                n += n&1
                result += 1
            n >>= 1
        return result