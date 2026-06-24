# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-of-minimum-values-in-all-subarrays
# source_path: LeetCode-Solutions-master/Python/maximum-of-minimum-values-in-all-subarrays.py
# solution_class: Solution
# submission_id: b1815cae1c0d88dfc9947d3aef3e1603f13d2ad0
# seed: 1531881436

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def findMaximums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def find_bound(nums, direction, init):
            result = [0]*len(nums)
            stk = [init]
            for i in direction(xrange(len(nums))):
                while stk[-1] != init and nums[stk[-1]] >= nums[i]:
                    stk.pop()
                result[i] = stk[-1]
                stk.append(i)
            return result

        left = find_bound(nums, lambda x: x, -1)
        right = find_bound(nums, reversed, len(nums))
        result = [-1]*len(nums)
        for i, v in enumerate(nums):
            result[((right[i]-1)-left[i])-1] = max(result[((right[i]-1)-left[i])-1], v)
        for i in reversed(xrange(len(nums)-1)):
            result[i] = max(result[i], result[i+1])
        return result