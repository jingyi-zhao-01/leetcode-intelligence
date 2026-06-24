# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-swaps-to-group-all-1s-together-ii
# source_path: LeetCode-Solutions-master/Python/minimum-swaps-to-group-all-1s-together-ii.py
# solution_class: Solution
# submission_id: 6e77a73d8788566c7ccf7d62490e707dfff4e512
# seed: 761947696

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = cnt = w = nums.count(1)
        for i in xrange(len(nums)+(w-1)):
            if i >= w:
                cnt += nums[(i-w)%len(nums)]
            cnt -= nums[i%len(nums)]
            result = min(result, cnt)
        return result