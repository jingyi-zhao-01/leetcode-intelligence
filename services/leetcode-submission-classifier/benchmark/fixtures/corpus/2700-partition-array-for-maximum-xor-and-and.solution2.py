# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-for-maximum-xor-and-and
# source_path: LeetCode-Solutions-master/Python/partition-array-for-maximum-xor-and-and.py
# solution_class: Solution2
# submission_id: 12128cbc6087d230acb6fa10358b4da7496a09eb
# seed: 703699646

# Time:  O(nlogr * 2^n)
# Space: O(2^n)

# bitmasks, greedy

class Solution2(object):
    def maximizeXorAndXor(self, nums):
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
        n = len(nums)
        result = 0
        for mask in xrange(1, 1<<n):
            and_arr = -1
            xor_arr = 0
            for i in xrange(n):
                if mask&(1<<i):
                    and_arr = and_arr&nums[i] if and_arr != -1 else nums[i]
                else:
                    xor_arr ^= nums[i]
            max_xor = max_xor_subset(((nums[i]&~xor_arr) for i in xrange(n) if not (mask&(1<<i))))
            result = max(result, and_arr+xor_arr+2*max_xor)
        return result