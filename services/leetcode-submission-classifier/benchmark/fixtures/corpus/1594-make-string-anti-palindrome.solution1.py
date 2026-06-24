# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-string-anti-palindrome
# source_path: LeetCode-Solutions-master/Python/make-string-anti-palindrome.py
# solution_class: Solution
# submission_id: f0202098d1be5e142a8d2e3736b776f32230d60f
# seed: 1420022448

# Time:  O(n + 26)
# Space: O(26)

# counting sort, greedy

class Solution(object):
    def makeAntiPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        if max(cnt) > len(s)//2:
            return "-1"
        result = [i for i, x in enumerate(cnt) for _ in xrange(x)]
        l = next(l for l in xrange((len(s)//2)//2+1) if result[len(s)//2+l] != result[len(s)//2-1])
        if l:
            for i in xrange(cnt[result[len(s)//2-1]]-l):
                result[len(s)//2+i], result[len(s)//2+i+l] = result[len(s)//2+i+l], result[len(s)//2+i]
        return "".join(map(lambda x: chr(ord('a')+x), result))