# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-imbalance-numbers-of-all-subarrays
# source_path: LeetCode-Solutions-master/Python/sum-of-imbalance-numbers-of-all-subarrays.py
# solution_class: Solution2
# submission_id: 552909e7ca8bdeda1bc6325ccad72e6387d5dac3
# seed: 1733055578

# Time:  O(n)
# Space: O(n)

# hash table, combinatorics

class Solution2(object):
    def sumImbalanceNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for right in xrange(len(nums)):
            lookup = {nums[right]}
            curr = 0
            for left in reversed(xrange(right)):
                if nums[left] not in lookup:
                    lookup.add(nums[left])
                    curr += 1-(nums[left]-1 in lookup)-(nums[left]+1 in lookup)
                result += curr
        return result