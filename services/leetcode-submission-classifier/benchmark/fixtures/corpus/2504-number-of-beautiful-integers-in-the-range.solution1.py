# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-beautiful-integers-in-the-range
# source_path: LeetCode-Solutions-master/Python/number-of-beautiful-integers-in-the-range.py
# solution_class: Solution
# submission_id: fb17a73a98f9e66e8f9f426f85eb7768c42caf39
# seed: 3320034933

# Time:  O(n^2 * k), n = len(str(high))
# Space: O(n^2 * k)

# memoization (faster but more space)

class Solution(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        :type low: int
        :type high: int
        :type k: int
        :rtype: int
        """
        TIGHT, UNTIGHT, UNBOUND = range(3)
        def f(x):
            digits = map(int, str(x))
            lookup = [[[[-1]*k for _ in xrange(2*len(digits)+1)] for _ in xrange(3)] for _ in xrange(len(digits))]
            def memoization(i, state, diff, total):
                if i == len(digits):
                    return int(state != UNBOUND and diff == total == 0)
                if lookup[i][state][diff][total] == -1:
                    result = int(i != 0 and diff == total == 0)  # count if the beautiful integer x s.t. len(str(x)) < len(digits)
                    for d in xrange(1 if i == 0 else 0, 10):
                        new_state = state
                        if state == TIGHT and d != digits[i]:
                            new_state = UNTIGHT if d < digits[i] else UNBOUND
                        new_diff = diff+(1 if d%2 == 0 else -1)
                        new_total = (total*10+d)%k
                        result += memoization(i+1, new_state, new_diff, new_total)
                    lookup[i][state][diff][total] = result
                return lookup[i][state][diff][total]
    
            return memoization(0, TIGHT, 0, 0)

        return f(high)-f(low-1)