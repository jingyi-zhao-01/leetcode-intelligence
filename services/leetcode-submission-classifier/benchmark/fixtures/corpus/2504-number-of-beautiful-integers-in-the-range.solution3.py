# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-beautiful-integers-in-the-range
# source_path: LeetCode-Solutions-master/Python/number-of-beautiful-integers-in-the-range.py
# solution_class: Solution3
# submission_id: 92c299788435944195ecd582722cc2ac7299eeb9
# seed: 2053997186

# Time:  O(n^2 * k), n = len(str(high))
# Space: O(n^2 * k)

# memoization (faster but more space)

class Solution3(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        :type low: int
        :type high: int
        :type k: int
        :rtype: int
        """
        def f(x):
            digits = map(int, str(x))
            lookup = [[[[[-1]*k for _ in xrange(2*len(digits)+1)] for _ in xrange(2)] for _ in xrange(2)] for _ in xrange(len(digits))]
            def memoization(i, zero, tight, diff, total):
                if i == len(digits):
                    return int(zero == diff == total == 0)
                if lookup[i][zero][tight][diff][total] == -1:
                    result = 0
                    for d in xrange((digits[i] if tight else 9)+1):
                        new_zero = int(zero and d == 0)
                        new_tight = int(tight and d == digits[i])
                        new_diff = diff+((1 if d%2 == 0 else -1) if new_zero == 0 else 0)
                        new_total = (total*10+d)%k
                        result += memoization(i+1, new_zero, new_tight, new_diff, new_total)
                    lookup[i][zero][tight][diff][total] = result
                return lookup[i][zero][tight][diff][total]
    
            return memoization(0, 1, 1, 0, 0)

        return f(high)-f(low-1)