# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longer-contiguous-segments-of-ones-than-zeros
# source_path: LeetCode-Solutions-master/Python/longer-contiguous-segments-of-ones-than-zeros.py
# solution_class: Solution
# submission_id: cf87ba253893411c2c9f412f1fefaae28f0c704e
# seed: 537484493

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_cnt = [0]*2
        cnt = 0
        for i in xrange(len(s)+1):
            if i == len(s) or (i >= 1 and s[i] != s[i-1]):
                max_cnt[int(s[i-1])] = max(max_cnt[int(s[i-1])], cnt)
                cnt = 0
            cnt += 1
        return max_cnt[0] < max_cnt[1]