# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-of-subsequences
# source_path: LeetCode-Solutions-master/Python/maximum-xor-of-subsequences.py
# solution_class: Solution
# submission_id: 954e606feee56d9f8327b9990e90052a94f4387d
# seed: 2954061500

# Time:  O(nlogr), r = max(nums)
# Space: O(r)

# bitmasks, greedy

class Solution(object):
    def maxXorSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def max_xor_subset(nums):  # Time: O(nlogr)
            base = [0]*l 
            for x in nums:  # gaussian elimination over GF(2)
                for b in base:
                    if x^b < x:
                        x ^= b
                if x:
                    base.append(x)
            max_xor = 0
            for b in base:  # greedy
                if (max_xor^b) > max_xor:
                    max_xor ^= b
            return max_xor

        l = max(nums).bit_length()
        return max_xor_subset(nums)