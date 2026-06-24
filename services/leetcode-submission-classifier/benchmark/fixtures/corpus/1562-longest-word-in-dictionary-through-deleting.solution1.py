# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-word-in-dictionary-through-deleting
# source_path: LeetCode-Solutions-master/Python/longest-word-in-dictionary-through-deleting.py
# solution_class: Solution
# submission_id: f4b9b0bfaa9b8bee1344b2b67b0399359540120a
# seed: 1093861825

# Time:  O((d * l) * logd), l is the average length of words
# Space: O(1)

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""