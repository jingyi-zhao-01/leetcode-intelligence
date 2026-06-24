# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-string-anti-palindrome
# source_path: LeetCode-Solutions-master/Python/make-string-anti-palindrome.py
# solution_class: Solution3
# submission_id: 611125265672ce5ae621e85183d9a6b205f8ec60
# seed: 1638308458

# Time:  O(n + 26)
# Space: O(26)

# counting sort, greedy

class Solution3(object):
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
        result = [-1]*len(s)
        for i in xrange(len(s)//2):
            j = next(j for j in xrange(len(cnt)) if cnt[j])
            cnt[j] -= 1
            result[i] = j
        for i in xrange(len(s)//2, len(s)):
            j = next(j for j in xrange(len(cnt)) if cnt[j] and result[(len(s)-1)-i] != j)
            cnt[j] -= 1
            result[i] = j
        return "".join(map(lambda x: chr(ord('a')+x), result))