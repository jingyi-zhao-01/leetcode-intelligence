# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-array-sum-using-divisible-replacements
# source_path: LeetCode-Solutions-master/Python/minimize-array-sum-using-divisible-replacements.py
# solution_class: Solution
# submission_id: b0b009efad59a4b99a2e68e629f09db2bea8b3cc
# seed: 810523420

# Time:  O(n + rlogr), r = max(nums)
# Space: O(r)

# number theory

class Solution(object):
    def minArraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        lookup = [0]*(mx+1)
        for x in nums:
            lookup[x] = x
        for i in xrange(1, mx+1):
            if not lookup[i]:
                continue
            for j in xrange(i+i, mx+1, i):
                if lookup[j] == j:
                    lookup[j] = i
        return sum(lookup[x] for x in nums)