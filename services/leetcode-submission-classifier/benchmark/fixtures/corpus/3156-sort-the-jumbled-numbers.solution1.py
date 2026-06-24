# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-the-jumbled-numbers
# source_path: LeetCode-Solutions-master/Python/sort-the-jumbled-numbers.py
# solution_class: Solution
# submission_id: 418c9847ad396589b0c63e9668f61eac82299074
# seed: 2624382737

# Time:  O(nlogm + nlogn), m is the max of nums
# Space: O(n)

# sort

class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def transform(mapping, x):
            if not x:
                return mapping[x]
            result, base = 0, 1
            while x:
                result += mapping[x%10]*base
                x //= 10
                base *= 10
            return result

        return [nums[i] for _, i in sorted((transform(mapping, nums[i]), i) for i in xrange(len(nums)))]