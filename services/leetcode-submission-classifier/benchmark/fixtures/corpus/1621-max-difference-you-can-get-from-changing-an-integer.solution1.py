# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-difference-you-can-get-from-changing-an-integer
# source_path: LeetCode-Solutions-master/Python/max-difference-you-can-get-from-changing-an-integer.py
# solution_class: Solution
# submission_id: 490ed7ac186dcb42e240c6f14d09090f05be8bf0
# seed: 1858300488

# Time:  O(logn)
# Space: O(1)

# greedy

class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        def find(num, check):
            result = 0
            while num:
                num, d = divmod(num, 10)
                if check(d):
                    result = d
            return result

        def reverse(num, l):
            result = 0
            while num or l > 0:
                num, d = divmod(num, 10)
                result = result*10+d
                l -= 1
            return result

        def replace(num, x, y):
            result = l = 0
            while num:
                num, d = divmod(num, 10)
                if d == x:
                    d = y
                result = result*10+d
                l += 1
            return reverse(result, l)
    
        b = find(num, lambda x: x < 9)
        a = find(num, lambda x: x > 1)
        return replace(num, b, 9)-replace(num, a, 1 if reverse(num, 0)%10 != 1 else 0)