# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-elements-with-frequency-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/sum-of-elements-with-frequency-divisible-by-k.py
# solution_class: Solution
# submission_id: 31b058d4a196ab4781bbe3978a6e15b334844171
# seed: 887789509

# Time:  O(n + r)
# Space: O(r)

# freq table

class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums)
        cnt = [0]*(mx+1)
        for x in nums:
            cnt[x] += 1
        return sum(x for x in nums if cnt[x]%k == 0)