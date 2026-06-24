# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-numbers-with-unique-digits-ii
# source_path: LeetCode-Solutions-master/Python/count-numbers-with-unique-digits-ii.py
# solution_class: Solution4
# submission_id: 28511586471fe661b72067d9c84145ee560eb611
# seed: 3517098454

# Time:  O(logb)
# Space: O(1)

# hash table, bitmasks, combinatorics

class Solution4(object):
    def numberCount(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum(len(set(str(x))) == len(str(x)) for x in xrange(a, b+1))