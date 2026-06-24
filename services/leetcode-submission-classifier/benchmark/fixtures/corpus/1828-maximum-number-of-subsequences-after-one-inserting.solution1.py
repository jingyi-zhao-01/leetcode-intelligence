# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-subsequences-after-one-inserting
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-subsequences-after-one-inserting.py
# solution_class: Solution
# submission_id: 927a2091fd173205fd6f9a6705250239894b2a64
# seed: 1880713098

# Time:  O(n)
# Space: O(1)

# prefix sum, dp

class Solution(object):
    def numOfSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt_l = cnt_c = 0
        cnt_t = s.count('T')
        mx_cnt_lt = cnt_lct = cnt_lc = cnt_ct = 0
        for x in s:
            mx_cnt_lt = max(mx_cnt_lt, cnt_l*cnt_t)
            if x == 'L':
                cnt_l += 1
            elif x == 'C':
                cnt_c += 1
                cnt_lc += cnt_l
            elif x == 'T':
                cnt_t -= 1
                cnt_ct += cnt_c
                cnt_lct += cnt_lc
        mx = max(mx_cnt_lt, cnt_l*cnt_t)
        return cnt_lct+max(cnt_ct, mx_cnt_lt, cnt_lc)