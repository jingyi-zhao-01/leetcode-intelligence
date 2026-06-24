# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: tuple-with-same-product
# source_path: LeetCode-Solutions-master/Python/tuple-with-same-product.py
# solution_class: Solution
# submission_id: f2c645281743b6a15d0f8d2429dd7a065828f7cb
# seed: 1883985441

# Time:  O(n^2)
# Space: O(n^2)

import collections

class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        count = collections.Counter()
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)): 
                result += count[nums[i]*nums[j]]
                count[nums[i]*nums[j]] += 1
        return 8*result