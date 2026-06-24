# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-maximum-mex-array
# source_path: LeetCode-Solutions-master/Python/lexicographically-maximum-mex-array.py
# solution_class: Solution2
# submission_id: 0b82865a4506ebccd06a83b8f274e5206fafd20a
# seed: 3630506101

# Time:  O(n)
# Space: O(n)

# hash table, prefix sum, greedy

class Solution2(object):
    def maximumMEX(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ver = -1
        lookup = [ver]*len(nums)
        cnt = [0]*len(nums)
        ver += 1
        mex = 0
        for i in xrange(len(nums)):
            if nums[i] < len(lookup):
                lookup[nums[i]] = ver
                cnt[nums[i]] += 1
            while mex < len(lookup) and lookup[mex] == ver:
                mex += 1
        new_suffix = suffix = mex
        result = []
        ver += 1
        mex = 0
        j = 0
        for i in xrange(len(nums)):
            if not suffix:
                break
            curr = 0
            if nums[i] < len(lookup):
                lookup[nums[i]] = ver
                cnt[nums[i]] -= 1
                if not cnt[nums[i]] and nums[i] < new_suffix:
                    new_suffix = nums[i]
            while mex < len(lookup) and lookup[mex] == ver:
                mex += 1
            if mex != suffix:
                continue
            result.append(mex)
            ver += 1
            mex = 0
            j = i+1
            suffix = new_suffix
        result.extend(0 for _ in xrange(len(nums)-j))
        return result