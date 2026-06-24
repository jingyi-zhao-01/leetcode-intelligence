# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-window-subsequence
# source_path: LeetCode-Solutions-master/Python/minimum-window-subsequence.py
# solution_class: Solution
# submission_id: bb72941a707ea0fc958a1e8f75ff8b3c4335c236
# seed: 2760812187

# Time:  O(s * t)
# Space: O(s)

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        lookup = [[None for _ in xrange(26)] for _ in xrange(len(S)+1)]
        find_char_next_pos = [None]*26
        for i in reversed(xrange(len(S))):
            find_char_next_pos[ord(S[i])-ord('a')] = i+1
            lookup[i] = list(find_char_next_pos)

        min_i, min_len = None, float("inf")
        for i in xrange(len(S)):
            if S[i] != T[0]:
                continue
            start = i
            for c in T:
                start = lookup[start][ord(c)-ord('a')]
                if start == None:
                    break
            else:
                if start-i < min_len:
                    min_i, min_len = i, start-i
        return S[min_i:min_i+min_len] if min_i is not None else ""