# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-missing-multiple-of-k
# source_path: LeetCode-Solutions-master/Python/smallest-missing-multiple-of-k.py
# solution_class: Solution
# submission_id: b5cb0eb15673090946197da67f7bee952ca5ddc9
# seed: 3328010582

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lookup = set(nums)
        for i in xrange(1, len(lookup)+1):
            if i*k not in lookup:
                return i*k
        return (len(lookup)+1)*k