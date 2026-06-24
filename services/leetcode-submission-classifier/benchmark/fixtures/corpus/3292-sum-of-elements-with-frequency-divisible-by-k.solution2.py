# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-elements-with-frequency-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/sum-of-elements-with-frequency-divisible-by-k.py
# solution_class: Solution2
# submission_id: 264811645340105594ec673171658e696899cbf2
# seed: 1549202601

# Time:  O(n + r)
# Space: O(r)

# freq table

class Solution2(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
        return sum(x for x in nums if cnt[x]%k == 0)