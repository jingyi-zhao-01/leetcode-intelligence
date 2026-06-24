# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsets-ii
# source_path: LeetCode-Solutions-master/Python/subsets-ii.py
# solution_class: Solution
# submission_id: 979169992db1251f2f52ebdc464f59e8d327cba2
# seed: 3638777193

# Time:  O(n * 2^n)
# Space: O(1)

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        previous_size = 0
        for i in xrange(len(nums)):
            size = len(result)
            for j in xrange(size):
                # Only union non-duplicate element or new union set.
                if i == 0 or nums[i] != nums[i - 1] or j >= previous_size:
                    result.append(list(result[j]))
                    result[-1].append(nums[i])
            previous_size = size
        return result