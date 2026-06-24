# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: range-addition
# source_path: LeetCode-Solutions-master/Python/range-addition.py
# solution_class: Solution
# submission_id: 726191f10156f797d44fbaece99d527ece0119f3
# seed: 3755659952

# Time:  O(k + n)
# Space: O(1)

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0] * length
        for update in updates:
            result[update[0]] += update[2]
            if update[1]+1 < length:
                result[update[1]+1] -= update[2]

        for i in xrange(1, length):
            result[i] += result[i-1]

        return result