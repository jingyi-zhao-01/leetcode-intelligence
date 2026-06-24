# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-missing-elements
# source_path: LeetCode-Solutions-master/Python/find-missing-elements.py
# solution_class: Solution
# submission_id: 124ee9b9c0214f9d314b4474f056a69283146830
# seed: 1786264661

# Time:  O(n + r)
# Space: O(n)

# hash table

class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lookup = set(nums)
        return [x for x in xrange(min(nums)+1, max(nums)) if x not in lookup]