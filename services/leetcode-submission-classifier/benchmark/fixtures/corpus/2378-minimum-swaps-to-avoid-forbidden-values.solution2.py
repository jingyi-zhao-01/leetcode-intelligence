# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-swaps-to-avoid-forbidden-values
# source_path: LeetCode-Solutions-master/Python/minimum-swaps-to-avoid-forbidden-values.py
# solution_class: Solution2
# submission_id: ea48e1b04e4db07525d539b5d0b7ce40dc64464b
# seed: 1907469252

# Time:  O(n)
# Space: O(1)

# boyer-moore majority vote algorithm, greedy

class Solution2(object):
    def minSwaps(self, nums, forbidden):
        """
        :type nums: List[int]
        :type forbidden: List[int]
        :rtype: int
        """
        cnt1 = collections.defaultdict(int)
        for x in nums:
            cnt1[x] += 1
        cnt2 = collections.defaultdict(int)
        for x in forbidden:
            cnt2[x] += 1
        if any(cnt1[k]+cnt2[k] > len(nums) for k in cnt1.iterkeys()):
            return -1
        cnt3 = collections.defaultdict(int)
        cnt = cnt_m = 0
        for i in xrange(len(nums)):
            if nums[i] != forbidden[i]:
                continue
            cnt += 1
            cnt3[nums[i]] += 1
            cnt_m = max(cnt_m, cnt3[nums[i]])
        return max(cnt_m, (cnt+1)//2)