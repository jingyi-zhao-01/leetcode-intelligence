# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: special-array-with-x-elements-greater-than-or-equal-x
# source_path: LeetCode-Solutions-master/Python/special-array-with-x-elements-greater-than-or-equal-x.py
# solution_class: Solution
# submission_id: 66b4667632b9f25c6a625f10e3b300ef35bc436e
# seed: 2979718585

# Time:  O(n)
# Space: O(1)

# counting sort solution

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_NUM = 1000
        count = [0]*(MAX_NUM+1)
        for num in nums:
            count[num] += 1
        n = len(nums)
        for i in xrange(len(count)):
            if i == n:
                return i
            n -= count[i]
        return -1