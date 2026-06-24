# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-operations-to-maximize-frequency-score
# source_path: LeetCode-Solutions-master/Python/apply-operations-to-maximize-frequency-score.py
# solution_class: Solution
# submission_id: cc97fc7d47d8fa621949904d46bca29e3f2143f7
# seed: 2484165873

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers, sliding window

class Solution(object):
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result = left = curr = 0
        for right in xrange(len(nums)):
            # "-+  " => "-0+ "
            # "-0+ " => "--++"
            curr += nums[right]-nums[(left+right)//2]
            if not curr <= k:
                # "--++" => " -0+"
                # " -0+" => "  -+"
                curr -= nums[((left+1)+right)//2]-nums[left]
                left += 1
        return right-left+1