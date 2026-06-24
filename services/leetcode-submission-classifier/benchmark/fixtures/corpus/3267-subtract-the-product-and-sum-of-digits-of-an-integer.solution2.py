# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subtract-the-product-and-sum-of-digits-of-an-integer
# source_path: LeetCode-Solutions-master/Python/subtract-the-product-and-sum-of-digits-of-an-integer.py
# solution_class: Solution2
# submission_id: 528a0cd86152d5973cd2511f5930d41b1e6bf09d
# seed: 4148587632

# Time:  O(logn)
# Space: O(1)

class Solution2(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        A = map(int, str(n))
        return reduce(operator.mul, A) - sum(A)