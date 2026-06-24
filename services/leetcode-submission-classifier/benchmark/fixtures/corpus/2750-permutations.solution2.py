# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutations
# source_path: LeetCode-Solutions-master/Python/permutations.py
# solution_class: Solution2
# submission_id: eebc148d36d9ce84a89d2eb7e23fc71ea1233d85
# seed: 2188606238

# Time:  O(n * n!)
# Space: O(n)

class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in xrange(len(nums)):
            # e.g., [1, 2, 3]: 3! = 6 cases
            # idx -> nums, path
            # 0 -> [2, 3], [1] -> 0: [3], [1, 2] -> [], [1, 2, 3]
            #                  -> 1: [2], [1, 3] -> [], [1, 3, 2]
            #
            # 1 -> [1, 3], [2] -> 0: [3], [2, 1] -> [], [2, 1, 3]
            #                  -> 1: [1], [2, 3] -> [], [2, 3, 1]
            #
            # 2 -> [1, 2], [3] -> 0: [2], [3, 1] -> [], [3, 1, 2]
            #                  -> 1: [1], [3, 2] -> [], [3, 2, 1]
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)