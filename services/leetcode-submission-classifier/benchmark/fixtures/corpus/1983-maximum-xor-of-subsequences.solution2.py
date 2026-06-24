# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-of-subsequences
# source_path: LeetCode-Solutions-master/Python/maximum-xor-of-subsequences.py
# solution_class: Solution2
# submission_id: 4d6b3869623328929ea24a58a82b061e19627a20
# seed: 2271151093

# Time:  O(nlogr), r = max(nums)
# Space: O(r)

# bitmasks, greedy

class Solution2(object):
    def maxXorSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def max_xor_subset(nums):  # Time: O(nlogr)
            base = [0]*l 
            for x in nums:  # gaussian elimination over GF(2)
                for i in reversed(xrange(len(base))):
                    if not x&(1<<i):
                        continue
                    if base[i] == 0:
                        base[i] = x
                        break
                    x ^= base[i]
            max_xor = 0
            for b in reversed(base):  # greedy
                if (max_xor^b) > max_xor:
                    max_xor ^= b
            return max_xor

        l = max(nums).bit_length()
        return max_xor_subset(nums)