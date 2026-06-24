# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-size-subarray-in-infinite-array
# source_path: LeetCode-Solutions-master/Python/minimum-size-subarray-in-infinite-array.py
# solution_class: Solution
# submission_id: c3053b4d94614f597e2f2988ab8a7860d53a9814
# seed: 3391829378

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        INF = float("inf")
        q, target = divmod(target, sum(nums))
        if not target:
            return q*len(nums)
        result = INF
        curr = left = 0
        for right in xrange((len(nums)-1)+(len(nums)-1)):
            curr += nums[right%len(nums)]
            while curr > target:
                curr -= nums[left%len(nums)]
                left += 1
            if curr == target:
                result = min(result, right-left+1)
        return result+q*len(nums) if result != INF else -1