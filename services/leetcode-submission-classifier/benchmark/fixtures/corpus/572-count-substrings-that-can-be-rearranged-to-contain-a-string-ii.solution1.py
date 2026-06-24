# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-that-can-be-rearranged-to-contain-a-string-ii
# source_path: LeetCode-Solutions-master/Python/count-substrings-that-can-be-rearranged-to-contain-a-string-ii.py
# solution_class: Solution
# submission_id: d1a486e4a2c4f525c402ff0ba2575bf05534f14e
# seed: 3791715204

# Time:  O(n + 26)
# Space: O(26)

# two pointers, sliding window, freq table

class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cnt = [0]*26
        curr = 0
        for x in word2:
            curr += int(cnt[ord(x)-ord('a')] == 0)
            cnt[ord(x)-ord('a')] += 1
        result = left = 0
        for right in xrange(len(word1)):
            cnt[ord(word1[right])-ord('a')] -= 1
            curr -= int(cnt[ord(word1[right])-ord('a')] == 0)
            while not curr:
                result += len(word1)-right
                curr += int(cnt[ord(word1[left])-ord('a')] == 0)
                cnt[ord(word1[left])-ord('a')] += 1
                left += 1
        return result