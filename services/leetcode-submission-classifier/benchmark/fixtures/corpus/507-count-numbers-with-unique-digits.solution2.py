# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-numbers-with-unique-digits
# source_path: LeetCode-Solutions-master/Python/count-numbers-with-unique-digits.py
# solution_class: Solution2
# submission_id: 4be53a480b18b2d775487c01fc1a69a3cfde39ea
# seed: 436315544

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact = [1]*2
        def nPr(n, k):
            while len(fact) <= n:  # lazy initialization
                fact.append(fact[-1]*len(fact))
            return fact[n]//fact[n-k]

        return 1+9*sum(nPr(9, i) for i in xrange(n))