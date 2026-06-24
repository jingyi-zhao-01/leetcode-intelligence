# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: set-mismatch
# source_path: LeetCode-Solutions-master/Python/set-mismatch.py
# solution_class: Solution
# submission_id: 56858aefcab8f84b7e29e0239a516aa138748e85
# seed: 3442929100

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x_xor_y = 0
        for i in xrange(len(nums)):
            x_xor_y ^= nums[i] ^ (i+1)
        bit = x_xor_y & ~(x_xor_y-1)
        result = [0] * 2
        for i, num in enumerate(nums):
            result[bool(num & bit)] ^= num
            result[bool((i+1) & bit)] ^= i+1
        if result[0] not in nums:
            result[0], result[1] = result[1], result[0]
        return result