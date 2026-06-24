# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-indices-with-opposite-parity
# source_path: LeetCode-Solutions-master/Python/count-indices-with-opposite-parity.py
# solution_class: Solution
# submission_id: dc58b36bd7456165cddda7ee47786ad58b7e58c4
# seed: 1877771915

# Time:  O(n)
# Space: O(1)

# freq table

class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        cnt = [0]*2
        for i in reversed(xrange(len(nums))):
            result[i] = cnt[1^(nums[i]%2)]
            cnt[nums[i]%2] += 1
        return result