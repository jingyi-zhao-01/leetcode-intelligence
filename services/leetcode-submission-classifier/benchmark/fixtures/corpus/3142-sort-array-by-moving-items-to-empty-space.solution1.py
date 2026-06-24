# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-array-by-moving-items-to-empty-space
# source_path: LeetCode-Solutions-master/Python/sort-array-by-moving-items-to-empty-space.py
# solution_class: Solution
# submission_id: 496cc7afc0687b8800f7fc4d5fb3ca6d8f421977
# seed: 75313376

# Time:  O(n)
# Space: O(n)

# greedy, sort

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def min_moves(d):
            def index(x):
                return d*(len(nums)-1) if x == 0 else x-d

            lookup = [False]*len(nums)
            result = len(nums)
            for i in xrange(len(nums)):
                if lookup[nums[i]]:
                    continue
                l = 0
                while not lookup[nums[i]]:
                    lookup[nums[i]] = True
                    l += 1
                    i = index(nums[i])
                result -= 1
                if l >= 2:
                    result += 2
            return result-2*int(nums[d*(len(nums)-1)] != 0)

        return min(min_moves(0), min_moves(1))