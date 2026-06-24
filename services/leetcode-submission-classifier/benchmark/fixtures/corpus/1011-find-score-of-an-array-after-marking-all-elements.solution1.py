# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-score-of-an-array-after-marking-all-elements
# source_path: LeetCode-Solutions-master/Python/find-score-of-an-array-after-marking-all-elements.py
# solution_class: Solution
# submission_id: ce597568a8d43aaf0371b1245eba6f13f3dfd86a
# seed: 1961129945

# Time:  O(nlogn)
# Space: O(n)

# simulation, sort, hash table

class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idxs = range(len(nums))
        idxs.sort(key=lambda x: (nums[x], x))
        lookup = [False]*len(nums)
        result = 0
        for i in idxs:
            if lookup[i]:
                continue
            lookup[i] = True
            if i-1 >= 0:
                lookup[i-1] = True
            if i+1 < len(lookup):
                lookup[i+1] = True
            result += nums[i]
        return result