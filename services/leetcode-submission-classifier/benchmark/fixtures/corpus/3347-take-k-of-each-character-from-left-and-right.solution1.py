# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: take-k-of-each-character-from-left-and-right
# source_path: LeetCode-Solutions-master/Python/take-k-of-each-character-from-left-and-right.py
# solution_class: Solution
# submission_id: a9b51973a7bf79c0b930018ea49e09e79348400b
# seed: 2702715364

# Time:  O(n)
# Space: O(1)

# sliding window, two pointers

class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = [0]*3
        for c in s:
            cnt[ord(c)-ord('a')] += 1
        if min(cnt) < k:
            return -1
        result = left = 0
        for right in xrange(len(s)):
            cnt[ord(s[right])-ord('a')] -= 1
            while cnt[ord(s[right])-ord('a')] < k:
                cnt[ord(s[left])-ord('a')] += 1
                left += 1
            result = max(result, right-left+1)
        return len(s)-result