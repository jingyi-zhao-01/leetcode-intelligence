# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-substring-with-at-most-k-distinct-characters
# source_path: LeetCode-Solutions-master/Python/longest-substring-with-at-most-k-distinct-characters.py
# solution_class: Solution2
# submission_id: 8f28393d76049b5ca7961d25dccddd5963b698d8
# seed: 1554061792

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = Counter()
        left, max_length = 0, 0
        for right, char in enumerate(s):
            counter[char] += 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length