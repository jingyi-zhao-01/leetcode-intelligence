# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-operations-to-make-string-empty
# source_path: LeetCode-Solutions-master/Python/apply-operations-to-make-string-empty.py
# solution_class: Solution
# submission_id: 83837d1fbd6f2e8943666379e4bec784a6bacb22
# seed: 1481494224

# Time:  O(n)
# Space: O(1)

# freq table

class Solution(object):
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        mx = max(cnt)
        result = []
        for x in reversed(s):
            if cnt[ord(x)-ord('a')] != mx:
                continue
            cnt[ord(x)-ord('a')] -= 1
            result.append(x)
        return "".join(reversed(result))