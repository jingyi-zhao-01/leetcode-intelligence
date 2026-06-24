# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-k-th-smallest-pair-distance
# source_path: LeetCode-Solutions-master/Python/find-k-th-smallest-pair-distance.py
# solution_class: Solution
# submission_id: d4d428487615d3ee4385e9eb2aef5904dc3afa2a
# seed: 133626056

# Time:  O(nlogn + nlogw), n = len(nums), w = max(nums)-min(nums)
# Space: O(1)

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sliding window solution
        def possible(guess, nums, k):
            count, left = 0, 0
            for right, num in enumerate(nums):
                while num-nums[left] > guess:
                    left += 1
                count += right-left
            return count >= k

        nums.sort()
        left, right = 0, nums[-1]-nums[0]+1
        while left < right:
            mid = left + (right-left)/2
            if possible(mid, nums, k):
                right = mid
            else:
                left = mid+1
        return left