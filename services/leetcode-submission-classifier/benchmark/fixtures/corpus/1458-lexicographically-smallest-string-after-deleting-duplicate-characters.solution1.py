# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-string-after-deleting-duplicate-characters
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-string-after-deleting-duplicate-characters.py
# solution_class: Solution
# submission_id: 40ea12d8b042169b6f09579b9f9664cff52f0f2a
# seed: 2929572857

# Time:  O(n + 26)
# Space: O(26)

# freq table, greedy

class Solution(object):
    def lexSmallestAfterDeletion(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        result = []
        for x in s:
            while result and result[-1] > x and cnt[ord(result[-1])-ord('a')] != 1:
                cnt[ord(result[-1])-ord('a')] -= 1
                result.pop()
            result.append(x)
        while cnt[ord(result[-1])-ord('a')] != 1:
            cnt[ord(result[-1])-ord('a')] -= 1
            result.pop()
        return "".join(result)