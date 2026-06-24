# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-pushes-to-type-word-i
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-pushes-to-type-word-i.py
# solution_class: Solution
# submission_id: 0611eee5de95e0a646ac464b4bbc6a70d52e3f50
# seed: 3045393920

# Time:  O(4)
# Space: O(1)

# greedy

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        return sum((i+1)*min(len(word)-i*(9-2+1), (9-2+1)) for i in xrange(ceil_divide(len(word), (9-2+1))))