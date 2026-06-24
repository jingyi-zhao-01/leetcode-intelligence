# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-powerful-integers
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-powerful-integers.py
# solution_class: Solution
# submission_id: f8833ae047c776b4628d8f90829a7fcc058f578a
# seed: 2323028849

# Time:  O(logf)
# Space: O(1)

# math, combinatorics

class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        def count(x):
            def length(x):
                result = 0
                while x:
                    x //= 10
                    result += 1
                return result

            result = 0
            n = length(x)
            base = 10**n
            l = n-len(s)
            cnt = (limit+1)**l
            for i in xrange(l):
                base //= 10
                curr = x//base%10
                cnt //= limit+1
                result += (min(curr-1, limit)-0+1)*cnt
                if curr > limit:
                    break
            else:
                if x%base >= int(s):
                    result += 1
            return result

        return count(finish)-count(start-1)