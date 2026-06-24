# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-number-and-its-reverse
# source_path: LeetCode-Solutions-master/Python/sum-of-number-and-its-reverse.py
# solution_class: Solution2
# submission_id: 35f3e7825ee8eaae3dcf641a216e93cc157b4da1
# seed: 2843464903

# Time:  O(2^(log10(n)/2)) = O(n^(1/(2*log2(10))))
# Space: O(log10(n)/2)

# backtracking

class Solution2(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def reverse(n):
            result = 0
            while n:
                result = result*10 + n%10
                n //= 10            
            return result

        return any(x+reverse(x) == num for x in xrange(num//2, num+1))