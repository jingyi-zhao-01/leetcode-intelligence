# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: patching-array
# source_path: LeetCode-Solutions-master/Python/patching-array.py
# solution_class: Solution3
# submission_id: bd6ede4e59a8fbcd453f97b56ab571f07fc81dce
# seed: 4224496186

# Time:  O(s + logn), s is the number of elements in the array
# Space: O(1)

class Solution3(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patch, miss, i = 0, 1, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patch += 1

        return patch