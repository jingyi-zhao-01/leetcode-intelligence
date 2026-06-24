# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutations-ii
# source_path: LeetCode-Solutions-master/Python/permutations-ii.py
# solution_class: Solution
# submission_id: a149bc54ebbe55cf12211b8ec53918a6f0be87bc
# seed: 2826340338

# Time:  O(n * n!)
# Space: O(n)

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(result, used, [], nums)
        return result

    def permuteUniqueRecu(self, result, used, cur, nums):
        if len(cur) == len(nums):
            result.append(cur + [])
            return
        for i in xrange(len(nums)):
            if used[i] or (i > 0 and nums[i-1] == nums[i] and not used[i-1]):
                continue
            used[i] = True
            cur.append(nums[i])
            self.permuteUniqueRecu(result, used, cur, nums)
            cur.pop()
            used[i] = False