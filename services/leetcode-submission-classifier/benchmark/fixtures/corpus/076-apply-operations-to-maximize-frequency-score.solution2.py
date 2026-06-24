# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-operations-to-maximize-frequency-score
# source_path: LeetCode-Solutions-master/Python/apply-operations-to-maximize-frequency-score.py
# solution_class: Solution2
# submission_id: f7ccac41ab4654a1c0b0580b88742b1cbd69ddc4
# seed: 2294290761

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers, sliding window

class Solution2(object):
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
            while not curr <= k:
                # "--++" => " -0+"
                # " -0+" => "  -+"
                curr -= nums[((left+1)+right)//2]-nums[left]
                left += 1
            result = max(result, right-left+1)
        return result