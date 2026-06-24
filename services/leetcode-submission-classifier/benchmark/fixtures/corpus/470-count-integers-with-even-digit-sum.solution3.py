# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-integers-with-even-digit-sum
# source_path: LeetCode-Solutions-master/Python/count-integers-with-even-digit-sum.py
# solution_class: Solution3
# submission_id: 8af086047fc6b5793bc147e64b9ffb4ea4ccf29e
# seed: 2956853309

# Time:  O(logn)
# Space: O(1)

# math

class Solution3(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        return sum(sum(map(int, str(x)))%2 == 0 for x in xrange(1, num+1))