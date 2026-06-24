# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-longest-special-substring-that-occurs-thrice-i
# source_path: LeetCode-Solutions-master/Python/find-longest-special-substring-that-occurs-thrice-i.py
# solution_class: Solution2
# submission_id: 89d844a9aa42d9ca21a13a1b146ddad2d70756ff
# seed: 2795536824

# Time:  O(26 * 3 + n * 3)
# Space: O(26 * 3)

# string, hash table

class Solution2(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = [[0] for _ in xrange(26)]
        result = 0
        for i, c in enumerate(s):
            curr = lookup[ord(c)-ord('a')]
            for j in xrange(i, len(s)):
                if s[j] != s[i]:
                    break
                if j-i+1 == len(curr):
                    curr.append(0)
                curr[j-i+1] += 1
                if curr[j-i+1] == 3:
                    result = max(result, j-i+1)
        return result if result else -1