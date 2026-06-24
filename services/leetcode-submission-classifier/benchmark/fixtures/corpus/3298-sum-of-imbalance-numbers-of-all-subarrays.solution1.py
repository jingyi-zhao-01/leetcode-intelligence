# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-imbalance-numbers-of-all-subarrays
# source_path: LeetCode-Solutions-master/Python/sum-of-imbalance-numbers-of-all-subarrays.py
# solution_class: Solution
# submission_id: 18793be1dfbd604bc897df46ad842024bc60da81
# seed: 3578519282

# Time:  O(n)
# Space: O(n)

# hash table, combinatorics

class Solution(object):
    def sumImbalanceNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = [len(nums)]*len(nums)
        lookup = [len(nums)]*((len(nums)+1)+1)
        for i in reversed(xrange(len(nums))):
            right[i] = min(lookup[nums[i]], lookup[nums[i]+1])  # to avoid duplicated count
            lookup[nums[i]] = i
        result = left = 0
        lookup = [-1]*((len(nums)+1)+1)
        for i in xrange(len(nums)):
            left = lookup[nums[i]+1]
            lookup[nums[i]] = i
            result += (i-left)*(right[i]-i)
        return result - (len(nums)+1)*len(nums)//2  # since we overcount 1 in each subarray, we have to subtract all of them