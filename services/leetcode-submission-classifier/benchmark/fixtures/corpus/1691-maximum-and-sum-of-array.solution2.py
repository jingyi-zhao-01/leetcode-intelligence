# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-and-sum-of-array
# source_path: LeetCode-Solutions-master/Python/maximum-and-sum-of-array.py
# solution_class: Solution2
# submission_id: ff7209cb6c80eff8ddcf0ed17885389a9dd55121
# seed: 49606917

# Time:  O(n^3)
# Space: O(n^2)

# weighted bipartite matching solution

class Solution2(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        adj = [[-((nums[i] if i < len(nums) else 0) & (1+x//2)) for x in xrange(2*numSlots)] for i in xrange(2*numSlots)]
        return -sum(adj[i][j] for i, j in itertools.izip(*hungarian(adj)))    