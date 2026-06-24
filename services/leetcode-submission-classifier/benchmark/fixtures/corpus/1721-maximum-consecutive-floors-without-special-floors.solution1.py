# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-consecutive-floors-without-special-floors
# source_path: LeetCode-Solutions-master/Python/maximum-consecutive-floors-without-special-floors.py
# solution_class: Solution
# submission_id: 199f3aeeccbc1157e4ec7486b0ba1a2eb1327063
# seed: 1820107262

# Time:  O(nlogn)
# Space: O(1)

# sort

class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        result = max(special[0]-bottom, top-special[-1])
        for i in xrange(1, len(special)):
            result = max(result, special[i]-special[i-1]-1)
        return result