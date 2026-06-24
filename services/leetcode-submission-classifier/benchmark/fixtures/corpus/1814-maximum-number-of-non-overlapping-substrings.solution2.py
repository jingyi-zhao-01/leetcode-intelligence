# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-non-overlapping-substrings
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-non-overlapping-substrings.py
# solution_class: Solution2
# submission_id: 98b17c11276c12b903f8a65a2a9f4de19765e2c0
# seed: 2312084594

# Time:  O(n)
# space: O(1)

class Solution2(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def find_right_from_left(s, first, last, left):
            right, i = last[ord(s[left])-ord('a')], left
            while i <= right:
                if first[ord(s[i])-ord('a')] < left:
                    return -1
                right = max(right, last[ord(s[i])-ord('a')])
                i += 1
            return right

        first, last = [float("inf")]*26, [float("-inf")]*26
        for i, c in enumerate(s):
            first[ord(c)-ord('a')] = min(first[ord(c)-ord('a')], i)
            last[ord(c)-ord('a')] = max(last[ord(c)-ord('a')], i)
        intervals = []
        for c in xrange(len(first)):
            if first[c] == float("inf"):
                continue
            left, right = first[c], find_right_from_left(s, first, last, first[c])
            if right != -1:
                intervals.append((right, left))
        intervals.sort()  # Time: O(26log26)
        result, prev = [], -1
        for right, left in intervals:
            if left <= prev:
                continue
            result.append(s[left:right+1])
            prev = right
        return result