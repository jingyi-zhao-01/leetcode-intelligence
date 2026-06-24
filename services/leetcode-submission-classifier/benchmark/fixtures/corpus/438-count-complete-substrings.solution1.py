# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-complete-substrings
# source_path: LeetCode-Solutions-master/Python/count-complete-substrings.py
# solution_class: Solution
# submission_id: 552c507a0c04373947024d15f202bca5ec5b3472
# seed: 192646822

# Time:  O(26 + d * n), d = len(set(word))
# Space: O(26)

# freq table, two pointers, sliding window

class Solution(object):
    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        result = valid = 0
        cnt = [0]*26
        for c in xrange(1, len(set(word))+1):
            left = 0
            for right in xrange(len(word)):
                cnt[ord(word[right])-ord('a')] += 1
                curr = cnt[ord(word[right])-ord('a')]
                valid += 1 if curr == k else -1 if curr == k+1 else 0
                if right-left+1 == c*k+1:
                    curr = cnt[ord(word[left])-ord('a')]
                    valid -= 1 if curr == k else -1 if curr == k+1 else 0
                    cnt[ord(word[left])-ord('a')] -= 1
                    left += 1
                if valid == c:
                    result += 1
                if right+1 == len(word) or abs(ord(word[right+1])-ord(word[right])) > 2:
                    while left < right+1:
                        curr = cnt[ord(word[left])-ord('a')]
                        valid -= 1 if curr == k else -1 if curr == k+1 else 0
                        cnt[ord(word[left])-ord('a')] -= 1
                        left += 1
        return result