# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: continuous-subarray-sum
# source_path: LeetCode-Solutions-master/Python/continuous-subarray-sum.py
# solution_class: Solution
# submission_id: 495524351b05da2570b950a505e96195fe23e314
# seed: 418464191

# Time:  O(n)
# Space: O(k)

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = 0
        lookup = {0: -1}
        for i, num in enumerate(nums):
            count += num
            if k:
                count %= k
            if count in lookup:
                if i - lookup[count] > 1:
                    return True
            else:
                lookup[count] = i

        return False