# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-ix
# source_path: LeetCode-Solutions-master/Python/jump-game-ix.py
# solution_class: Solution2
# submission_id: 1064ab5209445774a7bd21fa36ec2a5a403a3376
# seed: 1553085446

# Time:  O(n)
# Space: O(1)

# graph, prefix sum

class Solution2(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        suffix = [float("inf")]*(len(nums)+1)
        for i in reversed(xrange(len(nums))):
            suffix[i] = min(suffix[i+1], nums[i])
        result = [0]*len(nums)
        mx = left = 0
        for right in xrange(len(nums)):
            mx = max(mx, nums[right])
            if mx > suffix[right+1]:
                continue
            while left <= right:
                result[left] = mx
                left += 1
        return result