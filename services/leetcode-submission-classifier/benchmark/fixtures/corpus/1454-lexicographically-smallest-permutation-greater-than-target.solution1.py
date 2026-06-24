# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-permutation-greater-than-target
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-permutation-greater-than-target.py
# solution_class: Solution
# submission_id: c947733e9bb0357ef43737fee965908795b8db1f
# seed: 1714416637

# Time:  O(26 * n)
# Space: O(26)

# freq table, greedy

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        def nxt(cnt, x):
            for i in xrange(ord(x)-ord('a')+1, len(cnt)):
                if not cnt[i]:
                    continue
                return chr(ord('a')+i)
            return ' '

        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        tmp = cnt[:]
        j = -1
        for i, x in enumerate(target):
            y = nxt(tmp, x)
            if y != ' ':
                j = i
            if not tmp[ord(x)-ord('a')]:
                break
            tmp[ord(x)-ord('a')] -= 1
        if j == -1:
            return ""
        result = []
        for i in xrange(j):
            result.append(target[i])
            cnt[ord(target[i])-ord('a')] -= 1
        y = nxt(cnt, target[j])
        result.append(y)
        cnt[ord(y)-ord('a')] -= 1
        for i in xrange(len(cnt)):
            for _ in xrange(cnt[i]):
                result.append(chr(ord('a')+i))
                cnt[i] -= 1
        return "".join(result)