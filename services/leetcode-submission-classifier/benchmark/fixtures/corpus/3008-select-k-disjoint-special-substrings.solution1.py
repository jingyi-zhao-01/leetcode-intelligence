# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: select-k-disjoint-special-substrings
# source_path: LeetCode-Solutions-master/Python/select-k-disjoint-special-substrings.py
# solution_class: Solution
# submission_id: d406edec66e20ac19a64fe8761bcad7dd6a0b2c9
# seed: 3300520947

# Time:  O(n + 26^3)
# Space: O(26)

# hash table, sort, greedy

class Solution(object):
    def maxSubstringLength(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        def erase_overlap_intervals(intervals):
            intervals.sort(key=lambda interval: interval[1])
            result, right = 0, float("-inf")
            for l, r in intervals:
                if l <= right:
                    result += 1
                else:
                    right = r
            return result

        cnt = [0]*26
        lookup1, lookup2 = [-1]*26, [-1]*26
        for i, c in enumerate(s):
            cnt[ord(c)-ord('a')] += 1
            if lookup1[ord(c)-ord('a')] == -1:
                lookup1[ord(c)-ord('a')] = i
            lookup2[ord(c)-ord('a')] = i 
        intervals = []
        for i in lookup1:
            if i == -1:
                continue
            for j in lookup2:
                if j == -1 or i > j:
                    continue
                total = sum(cnt[c] for c in xrange(len(cnt)) if i <= lookup1[c] <= lookup2[c] <= j)
                if total == j-i+1 and total < len(s):
                    intervals.append((i, j))
        return len(intervals)-erase_overlap_intervals(intervals) >= k