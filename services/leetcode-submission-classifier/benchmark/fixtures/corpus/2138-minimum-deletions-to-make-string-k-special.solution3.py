# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-deletions-to-make-string-k-special
# source_path: LeetCode-Solutions-master/Python/minimum-deletions-to-make-string-k-special.py
# solution_class: Solution3
# submission_id: 10fc4d356573195c83923977c4c6bc29634ec004
# seed: 570017639

# Time:  O(n + 26)
# Space: O(n + 26)

# freq table, counting sort, two pointers

class Solution3(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        cnt = [0]*26
        for x in word:
            cnt[ord(x)-ord('a')] += 1
        return min(sum(y if y < x else max(y-(x+k), 0) for y in cnt if y) for x in cnt if x)