# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-replacements-to-sort-the-array
# source_path: LeetCode-Solutions-master/Python/minimum-replacements-to-sort-the-array.py
# solution_class: Solution
# submission_id: 7040b141070f8b752a116e947135ba27db0c0b58
# seed: 2274083458

# Time:  O(n)
# Space: O(1)

# greedy, math

class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        result = 0
        curr = nums[-1]
        for x in reversed(nums):
            cnt = ceil_divide(x, curr)
            result += cnt-1
            curr = x//cnt
        return result