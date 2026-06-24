# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-consistent-strings
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-consistent-strings.py
# solution_class: Solution
# submission_id: cc3db4909e0f60d920ac96533579dd9ad20a729b
# seed: 300600182

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        lookup = [False]*26
        for c in allowed:
            lookup[ord(c)-ord('a')] = True
        result = len(words)
        for word in words:
            for c in word:
                if not lookup[ord(c)-ord('a')]:
                    result -= 1
                    break
        return result