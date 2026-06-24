# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rabbits-in-forest
# source_path: LeetCode-Solutions-master/Python/rabbits-in-forest.py
# solution_class: Solution
# submission_id: 1e3583b58c0a4442080475afc293e20c8f09051b
# seed: 1951355049

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = collections.Counter(answers)
        return sum((((k+1)+v-1)//(k+1))*(k+1) for k, v in count.iteritems())