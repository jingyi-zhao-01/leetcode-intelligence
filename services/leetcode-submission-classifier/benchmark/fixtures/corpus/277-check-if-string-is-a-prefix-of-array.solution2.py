# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-string-is-a-prefix-of-array
# source_path: LeetCode-Solutions-master/Python/check-if-string-is-a-prefix-of-array.py
# solution_class: Solution2
# submission_id: b338b9c9fad17a26fbcba04bc904ac8b36b23fa4
# seed: 1381369008

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        i = 0
        for word in words:
            for c in word:
                if i == len(s) or s[i] != c:
                    return False
                i += 1
            if i == len(s):
                return True
        return False