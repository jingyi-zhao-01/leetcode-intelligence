# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-subarrays-after-removing-one-conflicting-pair
# source_path: LeetCode-Solutions-master/Python/maximize-subarrays-after-removing-one-conflicting-pair.py
# solution_class: Solution
# submission_id: 90c3d86a13341d63de9a15b1202229c5f9b9bbb4
# seed: 1733114628

# Time:  O(n + m)
# Space: O(n + m)

# greedy

class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        right = [[] for _ in xrange(n)]
        for l, r in conflictingPairs:
            l, r = l-1, r-1
            if l > r:
                l, r = r, l
            right[r].append(l)
        result = 0
        top2 = [-1]*2
        cnt = [0]*n
        for r in xrange(n):
            for l in right[r]:
                for i in xrange(len(top2)):
                    if l > top2[i]:
                        l, top2[i] = top2[i], l
            result += r-top2[0]
            if top2[0] != -1:
                cnt[top2[0]] += top2[0]-top2[1]
        return result+max(cnt)