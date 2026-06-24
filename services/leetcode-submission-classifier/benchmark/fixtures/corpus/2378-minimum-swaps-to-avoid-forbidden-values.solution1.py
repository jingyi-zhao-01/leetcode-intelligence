# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-swaps-to-avoid-forbidden-values
# source_path: LeetCode-Solutions-master/Python/minimum-swaps-to-avoid-forbidden-values.py
# solution_class: Solution
# submission_id: 7db716c67f0d66f0ab9976c36a0ab7c5a517108f
# seed: 199443981

# Time:  O(n)
# Space: O(1)

# boyer-moore majority vote algorithm, greedy

class Solution(object):
    def minSwaps(self, nums, forbidden):
        """
        :type nums: List[int]
        :type forbidden: List[int]
        :rtype: int
        """
        def boyer_moore_majority_vote(arr):
            result, cnt = None, 0
            for x in arr:
                if not cnt:
                    result = x
                if x == result:
                    cnt += 1
                else:
                    cnt -= 1
            return result

        m = boyer_moore_majority_vote((nums[i] for i in xrange(len(nums)) if nums[i] == forbidden[i]))
        cnt = cnt_m = bal = 0
        for i in xrange(len(nums)):
            if nums[i] != forbidden[i]:
                if nums[i] != m != forbidden[i]:
                    bal += 1
                continue
            cnt += 1
            if nums[i] != m:
                bal += 1
            else:
                bal -= 1
                cnt_m += 1
        return max(cnt_m, (cnt+1)//2) if bal >= 0 else -1