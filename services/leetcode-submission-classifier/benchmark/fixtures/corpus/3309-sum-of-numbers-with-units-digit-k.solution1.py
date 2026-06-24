# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-numbers-with-units-digit-k
# source_path: LeetCode-Solutions-master/Python/sum-of-numbers-with-units-digit-k.py
# solution_class: Solution
# submission_id: 2f64a7d69f797ef1fea51eae739c66f2541451b9
# seed: 1756649585

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def minimumNumbers(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        return next((i for i in xrange(1, (min(num//k, 10) if k else 1)+1) if (num-i*k)%10 == 0), -1) if num else 0