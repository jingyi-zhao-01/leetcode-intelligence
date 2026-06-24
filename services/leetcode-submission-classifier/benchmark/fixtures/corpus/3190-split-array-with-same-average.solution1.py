# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-array-with-same-average
# source_path: LeetCode-Solutions-master/Python/split-array-with-same-average.py
# solution_class: Solution
# submission_id: 486fdbfe99a6f05c06edeb2c05be74b9e646ba65
# seed: 1320368494

# Time:  O(n^4)
# Space: O(n^3)

class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def possible(total, n):
            for i in xrange(1, n//2+1):
                if total*i%n == 0:
                    return True
            return False
        n, s = len(A), sum(A)
        if not possible(n, s):
            return False

        sums = [set() for _ in xrange(n//2+1)]
        sums[0].add(0)
        for num in A:  # O(n) times
            for i in reversed(xrange(1, n//2+1)):  # O(n) times
                for prev in sums[i-1]:  # O(1) + O(2) + ... O(n/2) = O(n^2) times
                    sums[i].add(prev+num)
        for i in xrange(1, n//2+1):
            if s*i%n == 0 and s*i//n in sums[i]:
                return True
        return False