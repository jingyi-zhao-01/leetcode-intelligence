# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-maximum-mex-array
# source_path: LeetCode-Solutions-master/Python/lexicographically-maximum-mex-array.py
# solution_class: Solution
# submission_id: 3885e07d64636c35f5be9e8856092c79f24a40ad
# seed: 3403446984

# Time:  O(n)
# Space: O(n)

# hash table, prefix sum, greedy

class Solution(object):
    def maximumMEX(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ver = -1
        lookup = [ver]*len(nums)
        suffix = [0]*len(nums)
        ver += 1
        mex = 0
        for i in reversed(xrange(len(nums))):
            if nums[i] < len(lookup):
                lookup[nums[i]] = ver
            while mex < len(lookup) and lookup[mex] == ver:
                mex += 1
            suffix[i] = mex
        result = []
        ver += 1
        mex = 0
        j = 0
        for i in xrange(len(nums)):
            if not suffix[j]:
                break
            if nums[i] < len(lookup):
                lookup[nums[i]] = ver
            while mex < len(lookup) and lookup[mex] == ver:
                mex += 1
            if mex != suffix[j]:
                continue
            result.append(mex)
            ver += 1
            mex = 0
            j = i+1
        result.extend(0 for _ in xrange(len(nums)-j))
        return result