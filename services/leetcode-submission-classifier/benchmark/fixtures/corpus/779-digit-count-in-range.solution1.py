# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: digit-count-in-range
# source_path: LeetCode-Solutions-master/Python/digit-count-in-range.py
# solution_class: Solution
# submission_id: c44369ed09e7671396d72cf7cfec52dd40046ccc
# seed: 2473049820

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        def digitsCount(n, k):
            pivot, result = 1, 0
            while n >= pivot:
                result += (n//(10*pivot))*pivot + \
                           min(pivot, max(n%(10*pivot) - k*pivot + 1, 0))
                if k == 0:
                    result -= pivot
                pivot *= 10
            return result+1
        
        return digitsCount(high, d) - digitsCount(low-1, d)