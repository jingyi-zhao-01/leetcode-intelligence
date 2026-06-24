# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-array-empty
# source_path: LeetCode-Solutions-master/Python/make-array-empty.py
# solution_class: Solution
# submission_id: cbb8cf0911b589ad989a46ad69a216e46ab8d371
# seed: 1213039591

# Time:  O(nlogn)
# Space: O(n)

# sort

class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idxs = range(len(nums))
        idxs.sort(key=lambda x: nums[x])
        return len(idxs)+sum(len(idxs)-(i+1) for i in xrange(len(idxs)-1) if idxs[i] > idxs[i+1])