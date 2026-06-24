# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-and-sum-of-array
# source_path: LeetCode-Solutions-master/Python/maximum-and-sum-of-array.py
# solution_class: Solution4
# submission_id: c6e7e7b6b74efb65cf02bd4ee3a3050f349edc0b
# seed: 3243548328

# Time:  O(n^3)
# Space: O(n^2)

# weighted bipartite matching solution

class Solution4(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        def memoiztion(i, mask):  # i is metadata, which could be derived from mask, just for shorter implementation
            if lookup[mask] != -1:
                return lookup[mask]
            x = nums[i] if i < len(nums) else 0
            base = 1
            for slot in xrange(1, numSlots+1):
                if mask//base%3:
                     lookup[mask] = max(lookup[mask], (x&slot)+memoiztion(i-1, mask-base))
                base *= 3
            return lookup[mask]
        
        lookup = [-1]*(3**numSlots)
        lookup[0] = 0
        return memoiztion(2*numSlots-1, 3**numSlots-1)