# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-array-by-absolute-value
# source_path: LeetCode-Solutions-master/Python/sort-array-by-absolute-value.py
# solution_class: Solution
# submission_id: d157258f0b579892e561e1390ada8206866329c5
# seed: 54922192

# Time:  O(n + r)
# Space: O(n + r)

# sort

class Solution(object):
    def sortByAbsoluteValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mx = max(abs(x) for x in nums)
        lookup = [[] for _ in xrange(mx+1)]
        for x in nums:
            lookup[abs(x)].append(x)
        result = []
        for x in lookup:
            result.extend(x)
        return result