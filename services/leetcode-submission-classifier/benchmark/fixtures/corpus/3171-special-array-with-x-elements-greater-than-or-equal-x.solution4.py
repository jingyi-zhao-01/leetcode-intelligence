# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: special-array-with-x-elements-greater-than-or-equal-x
# source_path: LeetCode-Solutions-master/Python/special-array-with-x-elements-greater-than-or-equal-x.py
# solution_class: Solution4
# submission_id: e8cf0afa78dc1e11723545961c66bd31e5242adf
# seed: 1976281521

# Time:  O(n)
# Space: O(1)

# counting sort solution

class Solution4(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Time: O(nlogn)
        for i in xrange(len(nums)):  # Time: O(n)
            if nums[i] <= i:
                break
        else:
            i += 1
        return -1 if i < len(nums) and nums[i] == i else i