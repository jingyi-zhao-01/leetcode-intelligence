# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: relative-ranks
# source_path: LeetCode-Solutions-master/Python/relative-ranks.py
# solution_class: Solution
# submission_id: 4f296de4286ba5e9956885cf807b769fc8b768b3
# seed: 542444803

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_nums = sorted(nums)[::-1]
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sorted_nums, ranks)).get, nums)