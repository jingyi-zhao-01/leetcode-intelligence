# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-split-a-string
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-split-a-string.py
# solution_class: Solution
# submission_id: d72f6a56958651f2615f5bbf40d221b8183b7cb1
# seed: 3878598805

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9+7

        ones = s.count('1')
        if ones % 3:
            return 0
        ones //= 3
        if ones == 0:
            return (len(s)-1)*(len(s)-2)//2 % MOD
        count = left = right = 0
        for c in s:
            if c == '1':
                count += 1
            if count == ones:
                left += 1
            elif count == 2*ones:
                right += 1
        return left*right % MOD