# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: special-array-ii
# source_path: LeetCode-Solutions-master/Python/special-array-ii.py
# solution_class: Solution
# submission_id: 0f5fda7dbd937afa3253880b4889d8dd28399fd4
# seed: 2097484598

# Time:  O(n + q)
# Space: O(n)

# prefix sum

class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prefix = [0]*len(nums)
        for i in xrange(len(nums)-1):
            prefix[i+1] = prefix[i]+int(nums[i+1]&1 != nums[i]&1)
        result = [False]*len(queries)
        for i, (l, r) in enumerate(queries):
            result[i] = prefix[r]-prefix[l] == r-l
        return result