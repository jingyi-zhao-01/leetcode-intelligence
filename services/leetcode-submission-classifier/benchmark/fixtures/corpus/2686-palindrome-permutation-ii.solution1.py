# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-permutation-ii
# source_path: LeetCode-Solutions-master/Python/palindrome-permutation-ii.py
# solution_class: Solution
# submission_id: 5f58c7295408bf8e85b798278e233d797fc3e497
# seed: 3157526142

# Time:  O(n * n!)
# Space: O(n)

import collections
import itertools

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = ''.join(k for k, v in cnt.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())
        return self.permuteUnique(mid, chars) if len(mid) < 2 else []

    def permuteUnique(self, mid, nums):
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(mid, result, used, [], nums)
        return result

    def permuteUniqueRecu(self, mid, result, used, cur, nums):
        if len(cur) == len(nums):
            half_palindrome = ''.join(cur)
            result.append(half_palindrome + mid + half_palindrome[::-1])
            return
        for i in xrange(len(nums)):
            if not used[i] and not (i > 0 and nums[i-1] == nums[i] and used[i-1]):
                used[i] = True
                cur.append(nums[i])
                self.permuteUniqueRecu(mid, result, used, cur, nums)
                cur.pop()
                used[i] = False