# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-numbers-with-unique-digits-ii
# source_path: LeetCode-Solutions-master/Python/count-numbers-with-unique-digits-ii.py
# solution_class: Solution3
# submission_id: 20826ef776d181255b2a58613f812860404166f7
# seed: 751407630

# Time:  O(logb)
# Space: O(1)

# hash table, bitmasks, combinatorics

class Solution3(object):
    def numberCount(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def check(x):
            lookup = 0
            while x:
                if lookup&(1<<(x%10)):
                    return False
                lookup |= (1<<(x%10))
                x //= 10
            return True

        return sum(check(x) for x in xrange(a, b+1))