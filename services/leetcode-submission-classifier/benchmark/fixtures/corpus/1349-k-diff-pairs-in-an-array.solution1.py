# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-diff-pairs-in-an-array
# source_path: LeetCode-Solutions-master/Python/k-diff-pairs-in-an-array.py
# solution_class: Solution
# submission_id: 64c9d2790b0cb5da81b3e30ea857edd5382e4d8d
# seed: 2220916707

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        result, lookup = set(), set()
        for num in nums:
            if num-k in lookup:
                result.add(num-k)
            if num+k in lookup:
                result.add(num)
            lookup.add(num)
        return len(result)