# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-flips-to-make-a-or-b-equal-to-c
# source_path: LeetCode-Solutions-master/Python/minimum-flips-to-make-a-or-b-equal-to-c.py
# solution_class: Solution2
# submission_id: 1166f84661811e4ce224a92dac52862f27bbd19c
# seed: 3363721582

# Time:  O(31)
# Space: O(1)

class Solution2(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        result = 0
        for i in xrange(31):
            a_i, b_i, c_i = map(lambda x: x&1, [a, b, c])
            if (a_i | b_i) != c_i:
                result += 2 if a_i == b_i == 1 else 1
            a, b, c = a >> 1, b >> 1, c >> 1
        return result