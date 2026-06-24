# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-array-elements-by-sign
# source_path: LeetCode-Solutions-master/Python/rearrange-array-elements-by-sign.py
# solution_class: Solution3
# submission_id: f361dabfb8a20c7a8d45cb139abde5962f43b335
# seed: 1879855984

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution3(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos, neg = [], []
        for i in reversed(xrange(len(nums))):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        result = []
        for i in xrange(len(nums)):
            if i%2 == 0:
                result.append(pos.pop())
            else:
                result.append(neg.pop())
        return result