# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-missing-genetic-value-in-each-subtree
# source_path: LeetCode-Solutions-master/Python/smallest-missing-genetic-value-in-each-subtree.py
# solution_class: Solution
# submission_id: bff78ef4352d2b8623c4a79f160f7435de2c0018
# seed: 544442523

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def smallestMissingValueSubtree(self, parents, nums):
        """
        :type parents: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def iter_dfs(adj, nums, i, lookup):
            stk = [i]
            while stk:
                i = stk.pop()
                if nums[i] in lookup:
                    continue
                lookup.add(nums[i])
                for j in adj[i]:
                    stk.append(j)

        result = [1]*len(parents)
        i = next((i for i in xrange(len(nums)) if nums[i] == 1), -1)
        if i == -1:
            return result
        adj = [[] for _ in xrange(len(parents))]
        for j in xrange(1, len(parents)):
            adj[parents[j]].append(j)
        lookup = set()
        miss = 1
        while i >= 0:
            iter_dfs(adj, nums, i, lookup)
            while miss in lookup:
                miss += 1
            result[i] = miss
            i = parents[i]
        return result