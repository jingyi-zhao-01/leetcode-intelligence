# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: self-dividing-numbers
# source_path: LeetCode-Solutions-master/Python/self-dividing-numbers.py
# solution_class: Solution
# submission_id: d447b87427cfd30a07044c04c952a6e4b58448e3
# seed: 596536655

# Time:  O(nlogr) = O(n)
# Space: O(logr) = O(1)

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isDividingNumber(num):
            n = num
            while n > 0:
                n, r = divmod(n, 10)
                if r == 0 or (num%r) != 0:
                    return False
            return True
        
        return [num for num in xrange(left, right+1) if isDividingNumber(num)]