# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-triangle-number
# source_path: LeetCode-Solutions-master/Python/valid-triangle-number.py
# solution_class: Solution2
# submission_id: 390bca0f2860795522b89477176a9a7896a30f9a
# seed: 3604890678

# Time:  O(n^2)
# Space: O(1)

class Solution2(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in xrange(len(nums)-2):
            if nums[i] == 0:
                continue
            k = i+2
            for j in xrange(i+1, len(nums)-1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                result += k-j-1
        return result