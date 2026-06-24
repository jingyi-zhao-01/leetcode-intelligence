# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-lexicographically-smallest-array-by-swapping-elements
# source_path: LeetCode-Solutions-master/Python/make-lexicographically-smallest-array-by-swapping-elements.py
# solution_class: Solution
# submission_id: 6667d4b06e2077b5abc61e3ddcae22544e59ad45
# seed: 3181185416

# Time:  O(nlogn)
# Space: O(n)

# sort

class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        idxs = range(len(nums))
        idxs.sort(key=lambda x: nums[x])
        groups = []
        for i in xrange(len(nums)):
            if i-1 < 0 or nums[idxs[i]]-nums[idxs[i-1]] > limit:
                groups.append([])
            groups[-1].append(idxs[i])
        result = [-1]*len(nums)
        for g in groups:
            for i, j in enumerate(sorted(g)):
                result[j] = nums[g[i]]
        return result