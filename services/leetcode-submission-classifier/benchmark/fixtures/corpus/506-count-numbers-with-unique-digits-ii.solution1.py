# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-numbers-with-unique-digits-ii
# source_path: LeetCode-Solutions-master/Python/count-numbers-with-unique-digits-ii.py
# solution_class: Solution
# submission_id: 62e061864ac8fce238f98249ee13936d4c259e16
# seed: 3874370836

# Time:  O(logb)
# Space: O(1)

# hash table, bitmasks, combinatorics

class Solution(object):
    def numberCount(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def popcount(x):
            return bin(x).count('1')

        def count2(n):
            if n == 0:
                return 0
            result = cnt = 1
            for i in xrange(n-1):
                cnt *= 9-i
                result += cnt
            return 9*result

        def count(x):
            n = base = 1
            while x//(base*10):
                base *= 10
                n += 1
            result = count2(n-1)
            lookup = 0
            cnt = reduce(lambda accu, i: accu*(9-i), xrange(n-1), 1)
            for i in xrange(n):
                d = (x//base)%10
                base //= 10
                mask = lookup&(((1<<d)-1)-int(i == 0))
                result += ((d-int(i == 0))-popcount(mask))*cnt
                cnt //= 9-i
                if lookup&(1<<d):
                    break
                lookup |= 1<<d
            return result

        return count(b+1)-count(a)